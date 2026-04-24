from flask import Blueprint, jsonify, request

from ..extensions import db
from ..models import Seat, SessionEnrollment
from ..services.seat_allocator import allocate_seat, unassign_seat
from ..utils.validators import require_fields, require_positive_int

bp = Blueprint("seats", __name__, url_prefix="/api/seats")


@bp.get("/session/<int:sess_id>")
def list_session_seats(sess_id: int):
    seats = (
        db.session.query(Seat, SessionEnrollment.participant_id)
        .outerjoin(SessionEnrollment, Seat.seat_id == SessionEnrollment.seat_id)
        .filter(Seat.sess_id == sess_id)
        .order_by(Seat.seat_label.asc())
        .all()
    )
    return jsonify(
        {
            "success": True,
            "data": [
                {
                    "seat_id": seat.seat_id,
                    "sess_id": seat.sess_id,
                    "seat_label": seat.seat_label,
                    "is_accessible": bool(seat.is_accessible),
                    "is_active": bool(seat.is_active),
                    "participant_id": participant_id,
                }
                for seat, participant_id in seats
            ],
        }
    )


@bp.post("")
def create_seat():
    payload = request.get_json(silent=True) or {}
    require_fields(payload, ["sess_id", "seat_label"])
    sess_id = require_positive_int(payload["sess_id"], "sess_id")
    seat = Seat(
        sess_id=sess_id,
        seat_label=str(payload["seat_label"]).strip(),
        is_accessible=bool(payload.get("is_accessible", False)),
        is_active=bool(payload.get("is_active", True)),
    )
    db.session.add(seat)
    db.session.commit()
    return jsonify({"success": True, "data": {"seat_id": seat.seat_id}}), 201


@bp.post("/allocate")
def allocate():
    payload = request.get_json(silent=True) or {}
    require_fields(payload, ["sess_id", "participant_id"])
    try:
        result = allocate_seat(
            sess_id=payload["sess_id"],
            participant_id=payload["participant_id"],
            preferred_accessible=payload.get("preferred_accessible"),
        )
        return jsonify({"success": True, "data": result}), 201
    except ValueError as error:
        return jsonify({"success": False, "message": str(error)}), 409


@bp.post("/unassign")
def unassign():
    payload = request.get_json(silent=True) or {}
    require_fields(payload, ["sess_id", "participant_id"])
    try:
        result = unassign_seat(
            sess_id=payload["sess_id"],
            participant_id=payload["participant_id"],
        )
        return jsonify({"success": True, "data": result}), 200
    except ValueError as error:
        return jsonify({"success": False, "message": str(error)}), 404
