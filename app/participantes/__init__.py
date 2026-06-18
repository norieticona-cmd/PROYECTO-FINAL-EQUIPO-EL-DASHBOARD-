from flask import Blueprint

participante_bp = Blueprint(
    "participante",
    __name__
)

from app.participantes import routes
