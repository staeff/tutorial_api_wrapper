from . import session

class TV(object):
    def __init__(self, id):
        self.id = id

    def info(self):
        path = f'https://api.themoviedb.org/3/tv/{self.id}'
        response = session.get(path)
        return response.json()

    # staticmethod: does not need the class to be initialized to be
    # used. It does not use any instance variables and its called 
    # directly from the class.
    @staticmethod
    def popular():
        path = 'https://api.themoviedb.org/3/tv/popular'
        response = session.get(path)
        return response.json()
