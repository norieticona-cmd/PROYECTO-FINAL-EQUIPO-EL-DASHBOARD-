from app.extensions import db


class Premio(db.Model):

    __tablename__ = "premios"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nombre = db.Column(
        db.String(100),
        nullable=False
    )

    descripcion = db.Column(
        db.String(200)
    )

    proyecto_id = db.Column(
        db.Integer,
        db.ForeignKey("proyectos.id")
    )

    proyecto = db.relationship(
        "Proyecto",
        backref="premios"
    )