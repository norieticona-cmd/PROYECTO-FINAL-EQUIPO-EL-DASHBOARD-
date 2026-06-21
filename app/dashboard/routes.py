from flask_login import login_required
from flask import render_template
from sqlalchemy import func

from app.dashboard import dashboard_bp

from app.models.hackathon import Hackathon
from app.models.equipo import Equipo
from app.models.participante import Participante
from app.models.mentor import Mentor
from app.models.proyecto import Proyecto
from app.models.evaluacion import Evaluacion
from app.models.premio import Premio

from app.extensions import db

@dashboard_bp.route("/dashboard")
@login_required
def dashboard():

    total_hackathons = Hackathon.query.count()

    total_equipos = Equipo.query.count()

    total_participantes = Participante.query.count()

    total_mentores = Mentor.query.count()

    total_proyectos = Proyecto.query.count()

    total_evaluaciones = Evaluacion.query.count()

    promedio = db.session.query(
                    func.avg(Evaluacion.puntaje)
                ).scalar()

    mejor_evaluacion = Evaluacion.query.order_by(
                    Evaluacion.puntaje.desc()
                ).first()

    ultimo_premio = Premio.query.order_by(
                    Premio.id.desc()
                ).first()

    return render_template(
                    "dashboard/index.html",
                    total_hackathons=total_hackathons,
                    total_equipos=total_equipos,
                    total_participantes=total_participantes,
                    total_mentores=total_mentores,
                    total_proyectos=total_proyectos,
                    total_evaluaciones=total_evaluaciones,
                    promedio=promedio,
                    mejor_evaluacion=mejor_evaluacion,
                    ultimo_premio=ultimo_premio
                )