from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from views.movies import movie_ns
from views.directors import director_ns
from views.genres import genre_ns


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    configure_app(app)

    return app


def configure_app(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    create_data(app, db)


def create_data(app, db):
    with app.app_context():
        db.create_all()
        # db.session.add_all(db)
        # db.session.commit()


app = create_app(Config())

if __name__ == '__main__':
    app.run()
