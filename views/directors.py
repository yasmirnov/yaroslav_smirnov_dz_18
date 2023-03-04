from flask_restx import Resource, Namespace

from dao.models.director import DirectorSchema
from implemented import director_service

director_ns = Namespace('directors')

directors_schema = DirectorSchema(many=True)
director_schema = DirectorSchema()


@director_ns.route('/')
class DirectorsView(Resource):

    def get(self):
        all_directors = director_service.get_all()
        return directors_schema.dump(all_directors), 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):

    def get(self, did: int):
        director = director_service.get_one(did)
        return director_schema.dump(director), 200
