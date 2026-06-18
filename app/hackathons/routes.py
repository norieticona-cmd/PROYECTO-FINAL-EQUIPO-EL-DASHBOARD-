from flask import render_template
from flask import request
from flask import redirect

from flask_login import login_required

from app.hackathons import hackathon_bp

from app.extensions import db

from app.models.hackathon import Hackathon


@hackathon_bp.route("/hackathons")
@login_required
def listar_hackathons():

    hackathons = Hackathon.query.all()

    return render_template(
        "hackathons/listar.html",
        hackathons=hackathons
    )


@hackathon_bp.route(
    "/hackathons/nuevo",
    methods=["GET", "POST"]
)
@login_required
def nuevo_hackathon():

    if request.method == "POST":

        hackathon = Hackathon(
            nombre=request.form["nombre"],
            descripcion=request.form["descripcion"],
            estado=request.form["estado"]
        )

        db.session.add(hackathon)

        db.session.commit()

        return redirect("/hackathons")

    return render_template(
        "hackathons/nuevo.html"
    )

@hackathon_bp.route(
    "/hackathons/eliminar/<int:id>"
)
@login_required
def eliminar_hackathon(id):

    hackathon = Hackathon.query.get_or_404(id)

    db.session.delete(hackathon)

    db.session.commit()

    return redirect("/hackathons")

@hackathon_bp.route(
    "/hackathons/editar/<int:id>",
    methods=["GET", "POST"]
)
@login_required
def editar_hackathon(id):

    hackathon = Hackathon.query.get_or_404(id)

    if request.method == "POST":

        hackathon.nombre = request.form["nombre"]

        hackathon.descripcion = request.form["descripcion"]

        hackathon.estado = request.form["estado"]

        db.session.commit()

        return redirect("/hackathons")

    return render_template(
        "hackathons/editar.html",
        hackathon=hackathon
    )