from app.extensions import db

class Proyecto(db.Model):

    __tablename__ = "proyectos"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nombre = db.Column(
        db.String(150),
        nullable=False
    )

    descripcion = db.Column(
        db.Text,
        nullable=False
    )

    tecnologia = db.Column(
        db.String(100),
        nullable=False
    )

    estado = db.Column(
        db.String(50),
        default="En desarrollo"
    )

    equipo_id = db.Column(
        db.Integer,
        db.ForeignKey("equipos.id"),
        nullable=False
    )

    evaluaciones = db.relationship(
    "Evaluacion",
    backref="proyecto",
    lazy=True
)  

    def __repr__(self):
        return f"<Proyecto {self.nombre}>"