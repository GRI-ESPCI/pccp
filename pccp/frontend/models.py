from pccp.extensions import db

class Projet(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name = db.Column(
        db.String(255),
        info={"label": "Nom du projet"},
        nullable=False
    )
    slug = db.Column(
        db.String(255),
        info={"label": "Nom abrégé"},
        nullable=False
    )
    promo = db.Column(
        db.Integer,
        info={"label": "Promotion"}
    )
    courte_description = db.Column(
        db.String(255),
        info={"label": "Courte description"}
    )
    quoi = db.Column(
        db.Text,
        info={"label": "Quoi ?"}
    )
    ou = db.Column(
        db.Text,
        info={"label": "Où ?"}
    )
    pour_qui = db.Column(
        db.Text,
        info={"label": "Pour qui ?"}
    )
    pourquoi = db.Column(
        db.Text,
        info={"label": "Pourquoi ?"}
    )