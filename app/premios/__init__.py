from flask import Blueprint

premio_bp = Blueprint(
    "premios",
    __name__
)

from app.premios import routes
