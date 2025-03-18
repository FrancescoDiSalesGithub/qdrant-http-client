import requests


class endpoint:
    def __init__(self,host,port,apikey):
        self.host = host
        self.port = port
        self.apikey = apikey

    def __init__(self,host,port):
        self.host = host
        self.port = port