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

    # Keypoint

    keypoint1_icon = db.Column(
        db.String(255),
        info={"label": "Icône du point clé 1"},
        default=""
    )
    keypoint1_title = db.Column(
        db.String(255),
        info={"label": "Titre du point clé 1"},
        default=""
    )
    keypoint1_content = db.Column(
        db.String(255),
        info={"label": "Texte du point clé 1"},
        default=""
    )

    keypoint2_icon = db.Column(
        db.String(255),
        info={"label": "Icône du point clé 2"},
        default=""
    )
    keypoint2_title = db.Column(
        db.String(255),
        info={"label": "Titre du point clé 2"},
        default=""
    )
    keypoint2_content = db.Column(
        db.String(255),
        info={"label": "Texte du point clé 2"},
        default=""
    )

    keypoint3_icon = db.Column(
        db.String(255),
        info={"label": "Icône du point clé 3"},
        default=""
    )
    keypoint3_title = db.Column(
        db.String(255),
        info={"label": "Titre du point clé 3"},
        default=""
    )
    keypoint3_content = db.Column(
        db.String(255),
        info={"label": "Texte du point clé 3"},
        default=""
    )

    keypoint4_icon = db.Column(
        db.String(255),
        info={"label": "Icône du point clé 4"},
        default=""
    )
    keypoint4_title = db.Column(
        db.String(255),
        info={"label": "Titre du point clé 4"},
        default=""
    )
    keypoint4_content = db.Column(
        db.String(255),
        info={"label": "Texte du point clé 4"},
        default=""
    )

    # Chiffres

    chiffres1_icon = db.Column(
        db.String(255),
        info={"label": "Icône du chiffre 1"},
        default=""
    )
    chiffres1_title = db.Column(
        db.String(255),
        info={"label": "Titre du chiffre 1"},
        default=""
    )
    chiffres1_content = db.Column(
        db.String(255),
        info={"label": "Texte du chiffre 1"},
        default=""
    )

    chiffres2_icon = db.Column(
        db.String(255),
        info={"label": "Icône du chiffre 2"},
        default=""
    )
    chiffres2_title = db.Column(
        db.String(255),
        info={"label": "Titre du chiffre 2"},
        default=""
    )
    chiffres2_content = db.Column(
        db.String(255),
        info={"label": "Texte du chiffre 2"},
        default=""
    )

    chiffres3_icon = db.Column(
        db.String(255),
        info={"label": "Icône du chiffre 3"},
        default=""
    )
    chiffres3_title = db.Column(
        db.String(255),
        info={"label": "Titre du chiffre 3"},
        default=""
    )
    chiffres3_content = db.Column(
        db.String(255),
        info={"label": "Texte du chiffre 3"},
        default=""
    )

    chiffres4_icon = db.Column(
        db.String(255),
        info={"label": "Icône du chiffre 4"},
        default=""
    )
    chiffres4_title = db.Column(
        db.String(255),
        info={"label": "Titre du chiffre 4"},
        default=""
    )
    chiffres4_content = db.Column(
        db.String(255),
        info={"label": "Texte du chiffre 4"},
        default=""
    )