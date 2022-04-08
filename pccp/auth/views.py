from flask import Blueprint, render_template, current_app, request, flash, \
        url_for, redirect, session, abort, g
from flask_login import login_user, current_user, logout_user

from pccp.extensions import db, login_manager
from pccp.auth.models import User
from pccp.auth.forms import LoginForm

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('frontend.home'))

    form = LoginForm()
    if form.validate_on_submit():
        user, authenticated = User.authenticate(form.email.data, form.password.data)
        print(authenticated)
        if authenticated:
            login_user(user)
        flash("Nom d'utilisateur ou mot de passe invalide.")
        return redirect(url_for('auth.login'))

    return render_template('auth/login.html', form=form)
            

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('frontend.home'))

@login_manager.user_loader
def load_user(user_id):
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('frontend.home'))