from flask import render_template
from flask import request
from flask import redirect

from flask_login import login_required

from app.equipos import equipo_bp

from app.extensions import db

from app.models.equipo import Equipo
from app.models.hackathon import Hackathon


@equipo_bp.route("/equipos")
@login_required
def listar_equipos():

    equipos = Equipo.query.all()

    return render_template(
        "equipos/listar.html",
        equipos=equipos
    )


@equipo_bp.route(
    "/equipos/nuevo",
    methods=["GET", "POST"]
)
@login_required
def nuevo_equipo():

    if request.method == "POST":

        equipo = Equipo(
            nombre=request.form["nombre"],
            descripcion=request.form["descripcion"],
            hackathon_id=request.form["hackathon_id"]
        )

        db.session.add(equipo)

        db.session.commit()

        return redirect("/equipos")

    hackathons = Hackathon.query.all()

    return render_template(
        "equipos/nuevo.html",
        hackathons=hackathons
    )
    
@equipo_bp.route(
    "/equipos/editar/<int:id>",
    methods=["GET", "POST"]
)
@login_required
def editar_equipo(id):

    equipo = Equipo.query.get_or_404(id)

    if request.method == "POST":

        equipo.nombre = request.form["nombre"]

        equipo.descripcion = request.form["descripcion"]

        equipo.hackathon_id = request.form["hackathon_id"]

        db.session.commit()

        return redirect("/equipos")

    hackathons = Hackathon.query.all()

    return render_template(
        "equipos/editar.html",
        equipo=equipo,
        hackathons=hackathons
    )


@equipo_bp.route(
    "/equipos/eliminar/<int:id>"
)
@login_required
def eliminar_equipo(id):

    equipo = Equipo.query.get_or_404(id)

    db.session.delete(equipo)

    db.session.commit()

    return redirect("/equipos")
