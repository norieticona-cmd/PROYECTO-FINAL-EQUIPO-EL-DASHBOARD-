from flask import render_template
from flask_login import login_required

from app.premios import premio_bp

from app.models.premio import Premio
from flask import render_template, request, redirect
from app.extensions import db

from app.models.proyecto import Proyecto


@premio_bp.route("/premios")
@login_required
def listar_premios():

    premios = Premio.query.all()

    return render_template(
        "premios/listar.html",
        premios=premios
    )
    
@premio_bp.route("/premios/nuevo", methods=["GET", "POST"])
@login_required
def nuevo_premio():

    proyectos = Proyecto.query.all()

    if request.method == "POST":

        premio = Premio(
            nombre=request.form["nombre"],
            descripcion=request.form["descripcion"],
            proyecto_id=request.form["proyecto_id"]
        )

        db.session.add(premio)
        db.session.commit()

        return redirect("/premios")

    return render_template(
        "premios/nuevo.html",
        proyectos=proyectos
    )

@premio_bp.route(
    "/premios/editar/<int:id>",
    methods=["GET", "POST"]
)
@login_required
def editar_premio(id):

    premio = Premio.query.get_or_404(id)

    proyectos = Proyecto.query.all()

    if request.method == "POST":

        premio.nombre = request.form["nombre"]

        premio.descripcion = request.form["descripcion"]

        premio.proyecto_id = request.form["proyecto_id"]

        db.session.commit()

        return redirect("/premios")

    return render_template(
        "premios/editar.html",
        premio=premio,
        proyectos=proyectos
    )


@premio_bp.route(
    "/premios/eliminar/<int:id>"
)
@login_required
def eliminar_premio(id):

    premio = Premio.query.get_or_404(id)

    db.session.delete(premio)

    db.session.commit()

    return redirect("/premios")

    
    