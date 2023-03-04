from flask import request

from dao.models.movie import Movie
from dao.models.genre import Genre


class MovieDAO:

    def __init__(self, session):
        self.session = session

    def get_all(self):

        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        year = request.args.get('year')

        filters = {
            'director_id': director_id,
            'genre_id': genre_id,
            'year': year
        }

        if filters['director_id'] and filters['genre_id'] and filters['year']:
            return self.session.query(Movie).filter(Movie.director_id == filters['director_id']).filter(Movie.genre_id == filters['genre_id']).filter(Movie.year == filters['year']).all()
        elif filters['director_id']:
            return self.session.query(Movie).filter(Movie.director_id == filters['director_id']).all()
        elif filters['genre_id']:
            return self.session.query(Movie).filter(Movie.genre_id == filters['genre_id']).all()
        elif filters['year']:
            return self.session.query(Movie).filter(Movie.year == filters['year']).all()

        return self.session.query(Movie).all()

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def create(self, data):
        movie = Movie(**data)

        self.session.add(movie)
        self.session.commit()

        return movie

    def update(self, movie):

        self.session.add(movie)
        self.session.commit()

        return movie


    def delete(self, mid):
        movie = self.get_one(mid)

        self.session.delete(movie)
        self.session.commit()
