from flask import Blueprint, jsonify, request
from sqlalchemy import func

from ..extensions import db
from ..models import Division, DivisionParticipant, Participant
from ..utils.validators import parse_pagination, require_fields

bp = Blueprint("divisions", __name__, url_prefix="/api/divisions")

DIVISION_LIMITS = {
    "division a": 24,
    "division b": 18,
    "division c": 18,
}


@bp.get("")
def list_divisions():
    page, page_size = parse_pagination(request.args)
    manager_id = request.args.get("manager_id", type=int)
    query = Division.query
    if manager_id:
        query = query.filter_by(manager_id=manager_id)
    pagination = query.order_by(Division.div_id.asc()).paginate(page=page, per_page=page_size, error_out=False)
    return jsonify(
        {
            "success": True,
            "meta": {"page": page, "page_size": page_size, "total": pagination.total},
            "data": [
                {"div_id": division.div_id, "manager_id": division.manager_id, "name": division.name}
                for division in pagination.items
            ],
        }
    )


@bp.post("")
def create_division():
    payload = request.get_json(silent=True) or {}
    require_fields(payload, ["manager_id", "name"])
    normalized_name = str(payload["name"]).strip().lower()
    if normalized_name not in DIVISION_LIMITS:
        return (
            jsonify(
                {
                    "success": False,
                    "message": "Division name must be one of: Division A, Division B, Division C.",
                }
            ),
            400,
        )
    existing_same_name = (
        Division.query.filter(func.lower(Division.name) == normalized_name)
        .order_by(Division.div_id.asc())
        .first()
    )
    if existing_same_name:
        return jsonify({"success": False, "message": "This division already exists."}), 409

    division = Division(manager_id=payload["manager_id"], name=str(payload["name"]).strip())
    db.session.add(division)
    db.session.commit()
    return jsonify({"success": True, "data": {"div_id": division.div_id}}), 201


@bp.post("/<int:div_id>/participants")
def add_participant_to_division(div_id: int):
    payload = request.get_json(silent=True) or {}
    require_fields(payload, ["participant_id"])

    division = Division.query.get_or_404(div_id)
    Participant.query.get_or_404(payload["participant_id"])
    existing = DivisionParticipant.query.filter_by(
        div_id=div_id, participant_id=payload["participant_id"]
    ).first()
    if existing:
        return jsonify({"success": True, "message": "Participant already in division"}), 200

    division_limit = DIVISION_LIMITS.get(division.name.strip().lower())
    if division_limit is not None:
        current_count = DivisionParticipant.query.filter_by(div_id=div_id).count()
        if current_count >= division_limit:
            return (
                jsonify(
                    {
                        "success": False,
                        "message": f"{division.name} is full. Maximum participants: {division_limit}.",
                    }
                ),
                409,
            )

    association = DivisionParticipant(div_id=div_id, participant_id=payload["participant_id"])
    db.session.add(association)
    db.session.commit()
    return jsonify({"success": True, "message": "Participant added to division"}), 201


@bp.get("/<int:div_id>/participants")
def list_division_participants(div_id: int):
    Division.query.get_or_404(div_id)
    rows = (
        db.session.query(Participant)
        .join(DivisionParticipant, DivisionParticipant.participant_id == Participant.participant_id)
        .filter(DivisionParticipant.div_id == div_id)
        .order_by(Participant.participant_id.asc())
        .all()
    )
    return jsonify(
        {
            "success": True,
            "data": [
                {
                    "participant_id": participant.participant_id,
                    "first_name": participant.first_name,
                    "last_name": participant.last_name,
                    "email_address": participant.email_address,
                }
                for participant in rows
            ],
        }
    )
