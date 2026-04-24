from datetime import datetime

from ..extensions import db


class Session(db.Model):
    __tablename__ = "session"
    __table_args__ = (db.UniqueConstraint("div_id", "name", name="uq_session_division_name"),)

    sess_id = db.Column(db.Integer, primary_key=True)
    div_id = db.Column(
        db.Integer,
        db.ForeignKey("division.div_id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    name = db.Column(db.String(255), nullable=False)
    max_participants = db.Column(db.Integer, nullable=False)
    starts_at = db.Column(db.DateTime)
    ends_at = db.Column(db.DateTime)
    status = db.Column(db.String(20), nullable=False, default="scheduled")
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
