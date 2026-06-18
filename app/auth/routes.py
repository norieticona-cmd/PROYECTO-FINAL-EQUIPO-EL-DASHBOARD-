from flask import render_template
from flask import request
from flask import redirect

from flask_login import login_user
from flask_login import logout_user
from flask_login import current_user

from app.auth import auth_bp

from app.extensions import db
from app.extensions import bcrypt

from app.models.usuario import Usuario
from app.models.rol import Rol


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        usuario = Usuario.query.filter_by(
            username=username
        ).first()

        if usuario and bcrypt.check_password_hash(
            usuario.password,
            password
        ):

            login_user(usuario)

            return redirect("/dashboard")

        return "Usuario o contraseña incorrectos"

    return render_template(
        "auth/login.html"
    )


@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        password_hash = bcrypt.generate_password_hash(
            request.form["password"]
        ).decode("utf-8")

        rol_participante = Rol.query.filter_by(
            nombre="Participante"
        ).first()

        usuario = Usuario(
            nombre=request.form["nombre"],
            email=request.form["email"],
            username=request.form["username"],
            password=password_hash,
            rol_id=rol_participante.id
        )

        db.session.add(usuario)

        db.session.commit()

        return redirect("/login")

    return render_template(
        "auth/register.html"
    )


@auth_bp.route("/logout")
def logout():

    logout_user()

    return redirect("/login")