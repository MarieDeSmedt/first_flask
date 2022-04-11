from flask_sqlalchemy import SQLAlchemy

from .views import app 

import logging as lg

#create database connection object
db = SQLAlchemy(app)

class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable= False)
    genders = db.Column(db.Integer, )

    def __init__(self, description, gender):
        self.description = description
        self.gender = gender

def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(Content("info2",0))
    db.session.add(Content("info1",1))
    db.session.commit()
    lg.warning('db init')