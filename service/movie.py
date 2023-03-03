from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_by_filters(self):
        return self.dao.get_by_director()

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        mid = data.get('id')
        movie = self.get_one(mid)

        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year')
        movie.rating = data.get('rating')

        return self.dao.update(movie)

    def update_partial(self, data):
        mid = data.get('id')
        movie = self.get_one(mid)

        if 'title' in data:
            movie.title = data.get('title')
        if 'year' in data:
            movie.year = data.get('year')

        return self.dao.update(movie)

    def delete(self, mid):
        self.dao.delete(mid)
