from app.extensions import db


class Equipo(db.Model):

    __tablename__ = "equipos"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nombre = db.Column(
        db.String(100),
        nullable=False
    )

    descripcion = db.Column(
        db.Text,
        nullable=False
    )

    hackathon_id = db.Column(
        db.Integer,
        db.ForeignKey("hackathons.id"),
        nullable=False
    )
    
    participantes = db.relationship(
    "Participante",
    backref="equipo",
    lazy=True
    )

    proyectos = db.relationship(
    "Proyecto",
    backref="equipo",
    lazy=True
)


    def __repr__(self):
        return f"<Equipo {self.nombre}>"