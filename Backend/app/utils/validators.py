from flask import abort


def require_fields(payload: dict, fields: list[str]) -> None:
    missing = [field for field in fields if field not in payload or payload[field] in (None, "")]
    if missing:
        abort(400, description=f"Missing required fields: {', '.join(missing)}")


def require_positive_int(value, field_name: str) -> int:
    try:
        parsed = int(value)
    except (TypeError, ValueError):
        abort(400, description=f"{field_name} must be an integer")
    if parsed <= 0:
        abort(400, description=f"{field_name} must be greater than zero")
    return parsed


def parse_pagination(args) -> tuple[int, int]:
    page = require_positive_int(args.get("page", 1), "page")
    page_size = require_positive_int(args.get("page_size", 20), "page_size")
    if page_size > 100:
        abort(400, description="page_size cannot be greater than 100")
    return page, page_size
