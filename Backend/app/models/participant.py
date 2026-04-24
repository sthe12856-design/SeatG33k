from datetime import datetime

from ..extensions import db


class Participant(db.Model):
    __tablename__ = "participant"

    participant_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    contact_no = db.Column(db.String(30))
    email_address = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
