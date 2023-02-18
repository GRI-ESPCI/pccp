from flask import Blueprint, render_template, current_app, request, flash, \
        url_for, redirect, session, abort, g
from sqlalchemy import and_


from pccp.extensions import db
from pccp.frontend.models import Projet, IndexContent
from pccp.utils.bbcode import parse_bbcode

frontend = Blueprint('frontend', __name__)


@frontend.route('/')
def home():
    projets = Projet.query.filter(and_(
                Projet.is_visible == True,
                Projet.is_archive == False
            )).order_by(db.desc(Projet.promo)).all()
    ic = IndexContent.query.get(1)
    if ic is None:
        ic = IndexContent()
    return render_template('index.html', projets=projets, content=ic)

@frontend.route('/projet/<string:slug>')
def projet(slug):
    p = Projet.query.filter_by(slug=slug).first()
    print(p.name)
    if not p.is_visible:
        redirect("frontend.home")

    p.content = parse_bbcode(p.content)

    return render_template(
        'frontend/projet.html',
        projet=p
    )