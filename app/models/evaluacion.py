from app.extensions import db


class Evaluacion(db.Model):

    __tablename__ = "evaluaciones"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    puntaje = db.Column(
        db.Float,
        nullable=False
    )

    observacion = db.Column(
        db.Text
    )

    fecha = db.Column(
        db.String(20)
    )

    proyecto_id = db.Column(
        db.Integer,
        db.ForeignKey("proyectos.id"),
        nullable=False
    )

    def __repr__(self):
        return f"<Evaluacion {self.id}>"