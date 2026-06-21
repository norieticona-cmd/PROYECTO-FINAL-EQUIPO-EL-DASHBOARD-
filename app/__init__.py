from flask import Flask
from flask import Flask, render_template
from config import Config

from app.extensions import db
from app.extensions import bcrypt
from app.extensions import login_manager

from app.models import Rol
from app.models import Usuario
from app.models import Hackathon
from app.models import Participante
from app.models import Mentor
from app.models import Equipo
from app.models import Proyecto
from app.models import Evaluacion



from app.auth import auth_bp
from app.dashboard import dashboard_bp
from app.hackathons import hackathon_bp
from app.equipos import equipo_bp
from app.participantes import participante_bp
from app.mentores import mentor_bp
from app.proyectos import proyecto_bp
from app.evaluaciones import evaluacion_bp
from app.premios import premio_bp


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    bcrypt.init_app(app)

    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        return Usuario.query.get(int(user_id))

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(hackathon_bp)
    app.register_blueprint(equipo_bp)
    app.register_blueprint(participante_bp)
    app.register_blueprint(mentor_bp)
    app.register_blueprint(proyecto_bp)
    app.register_blueprint(evaluacion_bp)
    app.register_blueprint(premio_bp)
    
    
    with app.app_context():
        db.create_all()
        if Rol.query.count() == 0:

            db.session.add(
                Rol(nombre="Administrador")
            )

            db.session.add(
                Rol(nombre="Mentor")
            )

            db.session.add(
                Rol(nombre="Participante")
            )

            db.session.commit()

            print("Roles creados correctamente")

    @app.route("/")
    def home():
        return render_template("home.html")
        
    return app