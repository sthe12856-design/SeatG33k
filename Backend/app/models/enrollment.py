from datetime import datetime

from ..extensions import db


class SessionEnrollment(db.Model):
    __tablename__ = "session_enrollment"

    sess_id = db.Column(
        db.Integer,
        db.ForeignKey("session.sess_id", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
    )
    participant_id = db.Column(
        db.Integer,
        db.ForeignKey("participant.participant_id", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
    )
    seat_id = db.Column(
        db.Integer,
        db.ForeignKey("seat.seat_id", ondelete="SET NULL", onupdate="CASCADE"),
        unique=True,
    )
    enrolled_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
