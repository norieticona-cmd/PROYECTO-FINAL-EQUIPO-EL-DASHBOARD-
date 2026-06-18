from flask import Blueprint

evaluacion_bp = Blueprint(
    "evaluacion",
    __name__
)

from app.evaluaciones import routes