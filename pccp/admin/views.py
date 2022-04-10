import os

from flask import Blueprint, render_template, current_app, request, flash, \
        url_for, redirect, session, abort, g
from flask_login import login_required


from pccp.extensions import db
from pccp.frontend.models import Projet
from pccp.admin.forms import ProjetForm

admin = Blueprint('admin', __name__)


@admin.route('/admin/dashboard')
@login_required
def dashboard():
    projets_actifs = Projet.query.order_by(db.desc(Projet.promo)).limit(4).all()
    return render_template(
        "admin/dashboard.html",
        projets_actifs=projets_actifs
        )

@admin.route('/admin/projet/<string:slug>', methods=['GET', 'POST'])
@login_required
def projet(slug):
    p = Projet.query.filter_by(slug=slug).first()
    form = ProjetForm(obj=p)
    img_folder = 'static/img/projets/' + p.slug + '/'
    if form.validate_on_submit():
        form.populate_obj(p)
        db.session.add(p)
        db.session.commit()
        # Cover image
        if form.cover_img.data:
            img_data = request.files[form.cover_img.name].read()
            file_path = os.path.join(img_folder, p.slug + '_cover.jpg')
            if not os.path.exists(img_folder):
                os.mkdir(img_folder)
            open(file_path, "wb").write(img_data)
        # Thumbnail
        if form.thumbnail.data:
            img_data = request.files[form.thumbnail.name].read()
            file_path = os.path.join(img_folder, p.slug + '_thumbnail.jpg')
            if not os.path.exists(img_folder):
                os.mkdir(img_folder)
            open(file_path, "wb").write(img_data)
        return redirect(url_for('admin.projet', slug=p.slug))
    return render_template(
        "admin/projet.html",
        projet=p,
        form=form
    )