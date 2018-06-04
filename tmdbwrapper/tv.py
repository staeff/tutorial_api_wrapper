from . import session

class TV(object):
    def __init__(self, id):
        self.id = id

    def info(self):
        path = f'https://api.themoviedb.org/3/tv/{self.id}'
        response = session.get(path)
        return response.json()
