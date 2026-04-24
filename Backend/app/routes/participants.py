from flask import Blueprint, jsonify, request

from ..extensions import db
from ..models import Division, Participant, Seat, Session, SessionEnrollment
from ..utils.security import hash_password
from ..utils.validators import parse_pagination, require_fields

bp = Blueprint("participants", __name__, url_prefix="/api/participants")


@bp.get("")
def list_participants():
    page, page_size = parse_pagination(request.args)
    pagination = Participant.query.order_by(Participant.participant_id.asc()).paginate(
        page=page, per_page=page_size, error_out=False
    )
    return jsonify(
        {
            "success": True,
            "meta": {"page": page, "page_size": page_size, "total": pagination.total},
            "data": [
                {
                    "participant_id": participant.participant_id,
                    "first_name": participant.first_name,
                    "last_name": participant.last_name,
                    "email_address": participant.email_address,
                }
                for participant in pagination.items
            ],
        }
    )


@bp.get("/<int:participant_id>")
def get_participant(participant_id: int):
    participant = Participant.query.get_or_404(participant_id)
    return jsonify(
        {
            "success": True,
            "data": {
                "participant_id": participant.participant_id,
                "first_name": participant.first_name,
                "last_name": participant.last_name,
                "contact_no": participant.contact_no,
                "email_address": participant.email_address,
            },
        }
    )


@bp.post("")
def create_participant():
    payload = request.get_json(silent=True) or {}
    require_fields(payload, ["first_name", "last_name", "email_address", "password"])

    participant = Participant(
        first_name=payload["first_name"],
        last_name=payload["last_name"],
        contact_no=payload.get("contact_no"),
        email_address=str(payload["email_address"]).strip().lower(),
        password_hash=hash_password(payload["password"]),
    )
    db.session.add(participant)
    db.session.commit()

    return jsonify({"success": True, "data": {"participant_id": participant.participant_id}}), 201


@bp.get("/<int:participant_id>/sessions")
def get_participant_sessions(participant_id: int):
    Participant.query.get_or_404(participant_id)
    rows = (
        db.session.query(SessionEnrollment, Session, Division, Seat)
        .join(Session, Session.sess_id == SessionEnrollment.sess_id)
        .join(Division, Division.div_id == Session.div_id)
        .outerjoin(Seat, Seat.seat_id == SessionEnrollment.seat_id)
        .filter(SessionEnrollment.participant_id == participant_id)
        .order_by(Session.sess_id.asc())
        .all()
    )
    return jsonify(
        {
            "success": True,
            "data": [
                {
                    "sess_id": session.sess_id,
                    "session_name": session.name,
                    "division_id": division.div_id,
                    "division_name": division.name,
                    "status": session.status,
                    "seat_id": enrollment.seat_id,
                    "seat_label": seat.seat_label if seat else None,
                    "enrolled_at": enrollment.enrolled_at.isoformat() if enrollment.enrolled_at else None,
                }
                for enrollment, session, division, seat in rows
            ],
        }
    )
