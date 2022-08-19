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
    content = db.Column(
        db.Text,
        info={"label": "Contenu de la page"},
        default="",
        server_default=""
    )

    is_archive = db.Column(
        db.Boolean,
        nullable=False,
        default=False,
        server_default="false",
        info={"label": "Projet archivé ?"}
    )

    is_visible = db.Column(
        db.Boolean,
        nullable=False,
        default=False,
        server_default="false",
        info={"label": "Projet visible ?"}
    )


class IndexContent(db.Model):
    
    id = db.Column(
        db.Integer(),
        primary_key=True
    )

    bienvenue = db.Column(
        db.Text,
        info={"label": "Texte de bienvenue"},
        default="",
        server_default=""
    )

    don = db.Column(
        db.Text,
        info={"label": "Texte à côté du bouton de don"},
        default="",
        server_default=""
    )