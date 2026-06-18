from flask import Blueprint

proyecto_bp = Blueprint(
    "proyecto",
    __name__
)

from app.proyectos import routes