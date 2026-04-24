from datetime import datetime

from ..extensions import db


class DivisionParticipant(db.Model):
    __tablename__ = "division_participant"

    div_id = db.Column(
        db.Integer,
        db.ForeignKey("division.div_id", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
    )
    participant_id = db.Column(
        db.Integer,
        db.ForeignKey("participant.participant_id", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
    )
    joined_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
