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
    sections = db.relationship("ProjetSection", backref="projet", lazy=True, cascade="all, delete, delete-orphan")

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

class ProjetSection(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    title = db.Column(
        db.String(255),
        nullable=False,
        info={"label": "Titre de la section"}
    )
    content = db.Column(
        db.Text(),
        info={"label": "Contenu de la section"}
    )
    projet_id = db.Column(db.Integer, db.ForeignKey('projet.id'), nullable=False)