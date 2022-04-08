from flask import Blueprint, render_template, current_app, request, flash, \
        url_for, redirect, session, abort, g
from flask_login import login_required


from pccp.extensions import db

admin = Blueprint('admin', __name__)


@admin.route('/admin/dashboard')
@login_required
def dashboard():
    return "dashboard"