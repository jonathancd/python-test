import json

class Database():
    def __init__(self, json_url):
        self._json_url = json_url
        self._json_data = []

    @property
    def json_url(self):
        return self._json_url
    @property
    def json_data(self):
        return self._json_data
    
    @json_data.setter
    def json_data(self , json_data):
        self._json_data = json_data

    def load_data(self):
        with open(self.json_url) as f:
            return json.load(f)

    def save_data(self, json_data):
        with open(self.json_url, 'w') as f:
            json.dump(json_data, f, indent=4)