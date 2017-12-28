import requests


class ApiBaseObject(object):
    
    def __init__(self, *args, **kwargs):
        self.__dict__.update(kwargs)

    @classmethod
    def build_from(cls, url):
        response = requests.get(url)
        data = response.json()
        return cls(**data)