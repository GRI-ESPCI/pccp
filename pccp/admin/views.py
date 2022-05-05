import os
import re

from flask import Blueprint, render_template, current_app, request, flash, \
        url_for, redirect, session, abort, g
from flask_login import login_required


from pccp.extensions import db
from pccp.frontend.models import Projet, ProjetSection
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

@admin.route('/admin/projet/<string:slug>/edit', methods=['GET', 'POST'])
@login_required
def projet_edit(slug):
    p = Projet.query.filter_by(slug=slug).first()
    form = ProjetForm(obj=p)
    img_folder = 'static/img/projets/' + p.slug + '/'

    if form.validate_on_submit():
        form.populate_obj(p)

        submit_project_form(p, form, request)
        return redirect(url_for('admin.projet_edit', slug=p.slug))

    return render_template(
        "admin/projet_edit.html",
        projet=p,
        form=form
    )

@admin.route('/admin/projet/new', methods=['GET', 'POST'])
@login_required
def projet_new():
    form = ProjetForm()
    if form.validate_on_submit():
        p = Projet()
        form.populate_obj(p)
        img_folder = 'static/img/projets/' + p.slug + '/'

        submit_project_form(p, form, request)
        return redirect(url_for('admin.projet_edit', slug=p.slug))
    return render_template(
        "admin/projet_new.html",
        form=form
    )

def submit_project_form(p, form, request):
    img_folder = 'static/img/projets/' + p.slug + '/'

    # Projet sections
    del p.sections[:]
    is_section = re.compile(r"title-([0-9]+)")
    for field in request.form:
        res = is_section.search(field) 
        if res is not None:
            ps = ProjetSection()
            ps.title = request.form["title-" + res.group(1)]
            ps.content = request.form["content-" + res.group(1)]
            p.sections.append(ps)
            db.session.add(ps)

    db.session.add(p)
    db.session.commit()
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