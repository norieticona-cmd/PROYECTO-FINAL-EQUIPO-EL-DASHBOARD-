from flask import Blueprint

hackathon_bp = Blueprint(
    "hackathon",
    __name__
)

from app.hackathons import routes