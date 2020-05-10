import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json

database_path = os.environ['DATABASE_URL']
db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    migrate = Migrate(app, db)
    db.init_app(app)
    return db


def db_drop_and_create_all():
    db.drop_all()
    db.create_all()


class MovieCast(db.Model):
    __tablename__ = 'MovieCast'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('Movie.id', ondelete='CASCADE'), primary_key=True, unique=False, nullable=False)
    actor_id = db.Column(db.Integer, db.ForeignKey('Actor.id', ondelete='CASCADE'), primary_key=True, unique=False, nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()


class Movie(db.Model):
    __tablename__ = 'Movie'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(120), nullable=False)
    excerpt = db.Column(db.String(500), nullable=True)
    release_date = db.Column(db.Date, nullable=False)
    actors = db.relationship('MovieCast', passive_deletes=True, backref='movies', lazy=True)

    def long(self):
        return {
            'id': self.id,
            'title': self.title,
            'excerpt': self.excerpt,
            'release_date': self.release_date
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()


class Actor(db.Model):
    __tablename__ = 'Actor'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(60), nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=True)
    website = db.Column(db.String(120), nullable=True)
    movies = db.relationship('MovieCast', backref='actors', passive_deletes=True, lazy=True)

    def long(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'city': self.city,
            'state': self.state,
            'phone': self.phone,
            'email': self.email,
            'website': self.website
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()