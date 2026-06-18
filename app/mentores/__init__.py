from flask import Blueprint

mentor_bp = Blueprint(
    "mentor",
    __name__
)

from app.mentores import routes
