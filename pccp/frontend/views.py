from flask import Blueprint, render_template, current_app, request, flash, \
        url_for, redirect, session, abort, g


from pccp.extensions import db
from pccp.frontend.models import Projet

frontend = Blueprint('frontend', __name__)


@frontend.route('/')
def home():
    projets = Projet.query.order_by(db.desc(Projet.promo)).limit(4).all()
    return render_template('index.html', projets=projets)

@frontend.route('/projet/<string:slug>')
def projet(slug):
    p = Projet.query.filter_by(slug=slug).first()
    return render_template(
        'frontend/projet.html',
        projet=p
    )
