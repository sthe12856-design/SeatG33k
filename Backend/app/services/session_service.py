from ..extensions import db
from ..models import Session, SessionEnrollment


def get_session_availability(sess_id: int) -> dict:
    session = Session.query.get_or_404(sess_id)
    enrolled_count = SessionEnrollment.query.filter_by(sess_id=sess_id).count()
    return {
        "sess_id": session.sess_id,
        "name": session.name,
        "max_participants": session.max_participants,
        "enrolled_count": enrolled_count,
        "available_by_capacity": max(session.max_participants - enrolled_count, 0),
    }


def ensure_capacity(sess_id: int) -> None:
    availability = get_session_availability(sess_id)
    if availability["enrolled_count"] >= availability["max_participants"]:
        raise ValueError("Session capacity reached.")


def commit_or_rollback() -> None:
    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise
