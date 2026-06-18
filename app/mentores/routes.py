from flask import render_template
from flask import request
from flask import redirect

from flask_login import login_required

from app.mentores import mentor_bp

from app.extensions import db

from app.models.mentor import Mentor


@mentor_bp.route("/mentores")
@login_required
def listar_mentores():

    mentores = Mentor.query.all()

    return render_template(
        "mentores/listar.html",
        mentores=mentores
    )


@mentor_bp.route(
    "/mentores/nuevo",
    methods=["GET", "POST"]
)
@login_required
def nuevo_mentor():

    if request.method == "POST":

        mentor = Mentor(
            nombre=request.form["nombre"],
            especialidad=request.form["especialidad"],
            email=request.form["email"]
        )

        db.session.add(mentor)

        db.session.commit()

        return redirect("/mentores")

    return render_template(
        "mentores/nuevo.html"
    )
    
@mentor_bp.route(
    "/mentores/editar/<int:id>",
    methods=["GET", "POST"]
)
@login_required
def editar_mentor(id):

    mentor = Mentor.query.get_or_404(id)

    if request.method == "POST":

        mentor.nombre = request.form["nombre"]

        mentor.especialidad = request.form["especialidad"]

        mentor.email = request.form["email"]

        db.session.commit()

        return redirect("/mentores")

    return render_template(
        "mentores/editar.html",
        mentor=mentor
    )


@mentor_bp.route(
    "/mentores/eliminar/<int:id>"
)
@login_required
def eliminar_mentor(id):

    mentor = Mentor.query.get_or_404(id)

    db.session.delete(mentor)

    db.session.commit()

    return redirect("/mentores")
