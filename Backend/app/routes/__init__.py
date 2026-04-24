from flask import Blueprint, jsonify

api_bp = Blueprint("api", __name__)


@api_bp.get("")
def api_index():
    return jsonify(
        {
            "success": True,
            "message": "SeatG33k API",
            "endpoints": {
                "health": "/api/health",
                "managers": "/api/managers",
                "participants": "/api/participants",
                "divisions": "/api/divisions",
                "sessions": "/api/sessions",
                "seats": "/api/seats",
                "allocation": "/api/seats/allocate",
                "auth_login": "/api/auth/login",
            },
        }
    )


@api_bp.get("/health")
def health_check():
    return jsonify({"success": True, "message": "SeatG33k backend is running"})
