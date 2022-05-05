from flask import Blueprint, render_template, current_app, request, flash, \
        url_for, redirect, session, abort, g
from sqlalchemy import and_
import bbcode


from pccp.extensions import db
from pccp.frontend.models import Projet

frontend = Blueprint('frontend', __name__)


def _render_img(name, value, options, parent, context):
    if "alt" in options:
        alt = options['alt']
        return f'<div class="projet-center"><img alt="{alt}" src="{value}" /></div>'
    return value

def _render_map(name, value, options, parent, context):
    if "bbox" in options and "marker" in options:
        bbox = options['bbox']
        marker = options['marker']
        marker_data = marker.split('%2C')
        return f'<div class="projet-center"><iframe width="425" height="350" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://www.openstreetmap.org/export/embed.html?bbox={bbox}&amp;layer=mapnik&amp;marker={marker}" style="border: 1px solid black"></iframe><br/><small><a href="https://www.openstreetmap.org/?mlat={marker_data[0]}&amp;mlon={marker_data[1]}#map=16/47.6586/2.3446">Afficher une carte plus grande</a></small></div>'

    return value

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
    print(p.name)
    if not p.is_visible:
        redirect("frontend.home")

    parser = bbcode.Parser()
    parser.add_simple_formatter('h1', '<h1>%(value)s</h1>')
    parser.add_simple_formatter('h2', '<h2>%(value)s</h2>')
    parser.add_simple_formatter('h3', '<h3>%(value)s</h3>')
    parser.add_simple_formatter('b', '<b>%(value)s</b>')
    parser.add_simple_formatter('i', '<i>%(value)s</i>')
    parser.add_simple_formatter('u', '<u>%(value)s</u>')
    parser.add_simple_formatter('yt', '<div class="projet-center"><iframe class="projet-yt" width="560" height="315" src="https://www.youtube.com/embed/%(value)s" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>')
    parser.add_simple_formatter('ha', '<div class="projet-center"><iframe class="projet-ha" id="haWidget" allowtransparency="true" scrolling="auto" src="http://helloasso.com/%(value)s" onload="window.scroll(0, this.offsetTop)"></iframe></div>', replace_links=False)
    parser.add_formatter('img', _render_img, replace_links=False)
    parser.add_formatter('osm', _render_map, standalone=True)
    p.content = parser.format(p.content)

    return render_template(
        'frontend/projet.html',
        projet=p
    )