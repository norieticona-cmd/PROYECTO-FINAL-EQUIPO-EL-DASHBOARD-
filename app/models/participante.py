from app.extensions import db

class Participante(db.Model):

    __tablename__ = "participantes"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nombre = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(120),
        nullable=False
    )

    telefono = db.Column(
        db.String(30)
    )

    equipo_id = db.Column(
        db.Integer,
        db.ForeignKey("equipos.id"),
        nullable=False
    )

    def __repr__(self):
        return f"<Participante {self.nombre}>"