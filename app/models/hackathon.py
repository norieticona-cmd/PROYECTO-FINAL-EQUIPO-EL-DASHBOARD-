from app.extensions import db


class Hackathon(db.Model):

    __tablename__ = "hackathons"

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

    fecha_inicio = db.Column(
        db.Date
    )

    fecha_fin = db.Column(
        db.Date
    )

    estado = db.Column(
        db.String(30)
    )

    equipos = db.relationship(
    "Equipo",
    backref="hackathon",
    lazy=True
    )
    
    def __repr__(self):
        return f"<Hackathon {self.nombre}>"