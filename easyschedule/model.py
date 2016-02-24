# -*- coding: utf-8 -*-
#
#

from database import db


class User(db.Model):
    """Database model for SQLAlchemy."""
    id = db.Column(db.Integer, primary_key=True)
    ualogin = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)


    def __init__(self, ualogin, email):
        self.ualogin = ualogin
        self.email = email

    def __repr__(self):
        return '<User %r : %r>' % (self.ualogin, self.email)
