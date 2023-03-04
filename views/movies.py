from flask import request
from flask_restx import Resource, Namespace

from dao.models.movie import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')

movies_schema = MovieSchema(many=True)
movie_schema = MovieSchema()


@movie_ns.route('/')
class MoviesView(Resource):

    def get(self):
        all_movies = movie_service.get_all()
        return movies_schema.dump(all_movies), 200

    def post(self):
        req_json = request.json
        movie_service.create(req_json)
        return 'movie_added', 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):

    def get(self, mid: int):
        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie), 200

    def put(self, mid: int):
        req_json = request.json
        req_json['id'] = mid
        movie_service.update(req_json)
        return 'movie_upd', 204

    def delete(self, mid: int):
        movie_service.delete(mid)
        return 'movie_deleted', 204
