from flask import render_template
from flask import request
from flask import redirect

from flask_login import login_required

from app.evaluaciones import evaluacion_bp

from app.extensions import db

from app.models.evaluacion import Evaluacion
from app.models.proyecto import Proyecto


@evaluacion_bp.route("/evaluaciones")
@login_required
def listar_evaluaciones():

    evaluaciones = Evaluacion.query.all()

    return render_template(
        "evaluaciones/listar.html",
        evaluaciones=evaluaciones
    )


@evaluacion_bp.route(
    "/evaluaciones/nuevo",
    methods=["GET", "POST"]
)
@login_required
def nueva_evaluacion():

    if request.method == "POST":

        evaluacion = Evaluacion(
            puntaje=request.form["puntaje"],
            observacion=request.form["observacion"],
            fecha=request.form["fecha"],
            proyecto_id=request.form["proyecto_id"]
        )

        db.session.add(evaluacion)

        db.session.commit()

        return redirect("/evaluaciones")

    proyectos = Proyecto.query.all()

    return render_template(
        "evaluaciones/nuevo.html",
        proyectos=proyectos
    )
    
@evaluacion_bp.route(
    "/evaluaciones/editar/<int:id>",
    methods=["GET", "POST"]
)
@login_required
def editar_evaluacion(id):

    evaluacion = Evaluacion.query.get_or_404(id)

    if request.method == "POST":

        evaluacion.puntaje = request.form["puntaje"]

        evaluacion.observacion = request.form["observacion"]

        evaluacion.fecha = request.form["fecha"]

        evaluacion.proyecto_id = request.form["proyecto_id"]

        db.session.commit()

        return redirect("/evaluaciones")

    proyectos = Proyecto.query.all()

    return render_template(
        "evaluaciones/editar.html",
        evaluacion=evaluacion,
        proyectos=proyectos
    )


@evaluacion_bp.route(
    "/evaluaciones/eliminar/<int:id>"
)
@login_required
def eliminar_evaluacion(id):

    evaluacion = Evaluacion.query.get_or_404(id)

    db.session.delete(evaluacion)

    db.session.commit()

    return redirect("/evaluaciones")