from flask_restx import Resource, Namespace

from dao.models.genre import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genres')

genres_schema = GenreSchema(many=True)
genre_schema = GenreSchema()


@genre_ns.route('/')
class GenresView(Resource):

    def get(self):
        all_genres = genre_service.get_all()
        return genres_schema.dump(all_genres), 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):

    def get(self, gid: int):
        genre = genre_service.get_one(gid)
        return genre_schema.dump(genre), 200
