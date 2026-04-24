from datetime import datetime

from ..extensions import db


class Division(db.Model):
    __tablename__ = "division"
    __table_args__ = (db.UniqueConstraint("manager_id", "name", name="uq_division_manager_name"),)

    div_id = db.Column(db.Integer, primary_key=True)
    manager_id = db.Column(
        db.Integer,
        db.ForeignKey("manager.manager_id", ondelete="RESTRICT", onupdate="CASCADE"),
        nullable=False,
    )
    name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
