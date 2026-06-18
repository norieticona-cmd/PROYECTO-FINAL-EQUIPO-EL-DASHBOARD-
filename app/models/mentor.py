from app.extensions import db


class Mentor(db.Model):

    __tablename__ = "mentores"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nombre = db.Column(
        db.String(100),
        nullable=False
    )

    especialidad = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(120),
        nullable=False
    )

    def __repr__(self):
        return f"<Mentor {self.nombre}>"
    