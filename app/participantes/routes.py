from flask import render_template
from flask import request
from flask import redirect

from flask_login import login_required

from app.participantes import participante_bp

from app.extensions import db

from app.models.participante import Participante
from app.models.equipo import Equipo


@participante_bp.route("/participantes")
@login_required
def listar_participantes():

    participantes = Participante.query.all()

    return render_template(
        "participantes/listar.html",
        participantes=participantes
    )


@participante_bp.route(
    "/participantes/nuevo",
    methods=["GET", "POST"]
)
@login_required
def nuevo_participante():

    if request.method == "POST":

        participante = Participante(
            nombre=request.form["nombre"],
            email=request.form["email"],
            telefono=request.form["telefono"],
            equipo_id=request.form["equipo_id"]
        )

        db.session.add(participante)

        db.session.commit()

        return redirect("/participantes")

    equipos = Equipo.query.all()

    return render_template(
        "participantes/nuevo.html",
        equipos=equipos
    )
    

@participante_bp.route(
    "/participantes/editar/<int:id>",
    methods=["GET", "POST"]
)
@login_required
def editar_participante(id):

    participante = Participante.query.get_or_404(id)

    if request.method == "POST":

        participante.nombre = request.form["nombre"]
        participante.email = request.form["email"]
        participante.telefono = request.form["telefono"]
        participante.equipo_id = request.form["equipo_id"]

        db.session.commit()

        return redirect("/participantes")

    equipos = Equipo.query.all()

    return render_template(
        "participantes/editar.html",
        participante=participante,
        equipos=equipos
    )


@participante_bp.route(
    "/participantes/eliminar/<int:id>"
)
@login_required
def eliminar_participante(id):

    participante = Participante.query.get_or_404(id)

    db.session.delete(participante)

    db.session.commit()

    return redirect("/participantes")