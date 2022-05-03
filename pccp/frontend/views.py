from flask import Blueprint, render_template, current_app, request, flash, \
        url_for, redirect, session, abort, g
from sqlalchemy import and_


from pccp.extensions import db
from pccp.frontend.models import Projet

frontend = Blueprint('frontend', __name__)


@frontend.route('/')
def home():
    projets = Projet.query.filter(and_(
                Projet.is_visible == True,
                Projet.is_archive == False
            )).order_by(db.desc(Projet.promo)).limit(4).all()
    return render_template('index.html', projets=projets)

@frontend.route('/projet/<string:slug>')
def projet(slug):
    p = Projet.query.filter_by(slug=slug).first()
    if not p.is_visible:
        redirect("frontend.home")
    return render_template(
        'frontend/projet.html',
        projet=p
    )
