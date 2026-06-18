from flask import Blueprint

equipo_bp = Blueprint(
    "equipo",
    __name__
)

from app.equipos import routes
