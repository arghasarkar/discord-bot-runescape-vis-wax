import requests


class VisWaxCaller:

    def __init__(self, url):
        self.url = url

    def get_viswax_data(self):
        resp = requests.get(self.url)

        return resp
