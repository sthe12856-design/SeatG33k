from flask import Blueprint, jsonify, request

from ..extensions import db
from ..models import Session
from ..services.session_service import get_session_availability
from ..utils.validators import parse_pagination, require_fields, require_positive_int

bp = Blueprint("sessions", __name__, url_prefix="/api/sessions")

SESSION_LIMITS = {
    "morning session": 8,
    "midday session": 6,
    "afternoon session": 6,
}


@bp.get("")
def list_sessions():
    page, page_size = parse_pagination(request.args)
    div_id = request.args.get("div_id", type=int)
    status = request.args.get("status")
    query = Session.query
    if div_id:
        query = query.filter_by(div_id=div_id)
    if status:
        query = query.filter_by(status=status)
    pagination = query.order_by(Session.sess_id.asc()).paginate(page=page, per_page=page_size, error_out=False)
    return jsonify(
        {
            "success": True,
            "meta": {"page": page, "page_size": page_size, "total": pagination.total},
            "data": [
                {
                    "sess_id": session.sess_id,
                    "div_id": session.div_id,
                    "name": session.name,
                    "max_participants": session.max_participants,
                    "status": session.status,
                }
                for session in pagination.items
            ],
        }
    )


@bp.post("")
def create_session():
    payload = request.get_json(silent=True) or {}
    require_fields(payload, ["div_id", "name", "max_participants"])
    normalized_name = str(payload["name"]).strip().lower()
    if normalized_name not in SESSION_LIMITS:
        return (
            jsonify(
                {
                    "success": False,
                    "message": "Session name must be one of: Morning Session, Midday Session, Afternoon Session.",
                }
            ),
            400,
        )

    provided_max = require_positive_int(payload["max_participants"], "max_participants")
    required_max = SESSION_LIMITS[normalized_name]
    if provided_max != required_max:
        return (
            jsonify(
                {
                    "success": False,
                    "message": f"{payload['name']} must have max_participants set to {required_max}.",
                }
            ),
            400,
        )

    same_name_count = Session.query.filter(db.func.lower(Session.name) == normalized_name).count()
    if same_name_count >= 3:
        return jsonify({"success": False, "message": f"Maximum of 3 '{payload['name']}' entries reached."}), 409

    session = Session(
        div_id=payload["div_id"],
        name=str(payload["name"]).strip(),
        max_participants=required_max,
        status=payload.get("status", "scheduled"),
    )
    db.session.add(session)
    db.session.commit()
    return jsonify({"success": True, "data": {"sess_id": session.sess_id}}), 201


@bp.patch("/<int:sess_id>/status")
def update_session_status(sess_id: int):
    payload = request.get_json(silent=True) or {}
    require_fields(payload, ["status"])
    allowed = {"scheduled", "open", "closed", "cancelled"}
    if payload["status"] not in allowed:
        return jsonify({"success": False, "message": "Invalid session status"}), 400

    session = Session.query.get_or_404(sess_id)
    session.status = payload["status"]
    db.session.commit()
    return jsonify({"success": True, "message": "Session status updated"})


@bp.get("/<int:sess_id>/capacity")
def get_capacity(sess_id: int):
    return jsonify({"success": True, "data": get_session_availability(sess_id)})
