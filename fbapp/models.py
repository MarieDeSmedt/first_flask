from flask_sqlalchemy import SQLAlchemy

from .views import app 
import enum
import logging as lg

#create database connection object
db = SQLAlchemy(app)

class Gender(enum.Enum):
    female = 0
    male = 1
    other = 2

class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable= False)
    gender = db.Column(db.Enum(Gender))

    def __init__(self, description, gender="female"):
        self.description = description
        self.gender = gender


def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(Content("description pour homme1",Gender['male']))
    db.session.add(Content("description pour femme1",Gender['female']))
    db.session.add(Content("description pour homme2",Gender['male']))
    db.session.add(Content("description pour femme2",Gender['female']))
    db.session.add(Content("description pour homme3",Gender['male']))
    db.session.add(Content("description pour femme3",Gender['female']))
    db.session.commit()
    lg.warning('db init')