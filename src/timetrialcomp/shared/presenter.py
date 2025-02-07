from datetime import datetime

from src.shared.domain.errors import DomainError


def render_timestamp(dt: datetime) -> str:
    timestamp = str(dt.timestamp()).split(".")[0]
    return f"<t:{timestamp}>"


def render_error_message(error: DomainError):
    return f"```ERROR: {error.message}```"
