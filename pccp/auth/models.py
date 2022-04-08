from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from pccp.extensions import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128))
    email = db.Column(db.String(255), unique=True)

    _password = db.Column('password', db.String(200))

    def _get_password(self):
        return self._password

    def _set_password(self, password):
        self._password = generate_password_hash(password)

    password = db.synonym('_password', descriptor=property(_get_password, _set_password))

    def check_password(self, password):
        if self.password is None:
            return False
        return check_password_hash(self.password, password)

    @classmethod
    def authenticate(cls, login, password):
        user = cls.query.filter(db.or_(
            User.username == login, User.email == login
        )).first()

        if user:
            authenticated = user.check_password(password)
        else:
            authenticated = False
        
        return user, authenticated
