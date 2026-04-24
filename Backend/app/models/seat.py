from ..extensions import db


class Seat(db.Model):
    __tablename__ = "seat"
    __table_args__ = (db.UniqueConstraint("sess_id", "seat_label", name="uq_seat_session_label"),)

    seat_id = db.Column(db.Integer, primary_key=True)
    sess_id = db.Column(
        db.Integer,
        db.ForeignKey("session.sess_id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    seat_label = db.Column(db.String(50), nullable=False)
    is_accessible = db.Column(db.Boolean, nullable=False, default=False)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
