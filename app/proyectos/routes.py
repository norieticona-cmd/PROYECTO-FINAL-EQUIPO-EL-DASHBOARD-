from flask import render_template
from flask import request
from flask import redirect

from flask_login import login_required

from app.proyectos import proyecto_bp

from app.extensions import db

from app.models.proyecto import Proyecto
from app.models.equipo import Equipo


@proyecto_bp.route("/proyectos")
@login_required
def listar_proyectos():

    proyectos = Proyecto.query.all()

    return render_template(
        "proyectos/listar.html",
        proyectos=proyectos
    )


@proyecto_bp.route(
    "/proyectos/nuevo",
    methods=["GET", "POST"]
)
@login_required
def nuevo_proyecto():

    if request.method == "POST":

        proyecto = Proyecto(
            nombre=request.form["nombre"],
            descripcion=request.form["descripcion"],
            tecnologia=request.form["tecnologia"],
            estado=request.form["estado"],
            equipo_id=request.form["equipo_id"]
        )

        db.session.add(proyecto)

        db.session.commit()

        return redirect("/proyectos")

    equipos = Equipo.query.all()

    return render_template(
        "proyectos/nuevo.html",
        equipos=equipos
    )

@proyecto_bp.route(
    "/proyectos/editar/<int:id>",
    methods=["GET", "POST"]
)
@login_required
def editar_proyecto(id):

    proyecto = Proyecto.query.get_or_404(id)

    if request.method == "POST":

        proyecto.nombre = request.form["nombre"]

        proyecto.descripcion = request.form["descripcion"]

        proyecto.tecnologia = request.form["tecnologia"]

        proyecto.estado = request.form["estado"]

        proyecto.equipo_id = request.form["equipo_id"]

        db.session.commit()

        return redirect("/proyectos")

    equipos = Equipo.query.all()

    return render_template(
        "proyectos/editar.html",
        proyecto=proyecto,
        equipos=equipos
    )


@proyecto_bp.route(
    "/proyectos/eliminar/<int:id>"
)
@login_required
def eliminar_proyecto(id):

    proyecto = Proyecto.query.get_or_404(id)

    db.session.delete(proyecto)

    db.session.commit()

    return redirect("/proyectos")