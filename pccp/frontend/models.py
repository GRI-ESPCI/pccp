from pccp.extensions import db

class Projet(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(255), nullable=False)
    promo = db.Column(db.Integer)
    courte_description = db.Column(db.String(255))
    quoi = db.Column(db.Text)
    ou = db.Column(db.Text)
    pour_qui = db.Column(db.Text)
    pourquoi = db.Column(db.Text)