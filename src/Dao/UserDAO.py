from Database.Database import Database
from Models.User import User

class UserDAO:
    def __init__(self):
        self._json_url = 'src/json/users.json'

    @property
    def json_url(self):
        return self._json_url

    @json_url.setter
    def json_url(self , json_url):
        self._json_url = json_url

    def index(self):
        items = list()
        db = Database(self.json_url)
        rows = db.load_data()

        if isinstance(rows, list):
            for row in rows:
                user = User(row['age'], row['email'], row['names'], row['surnames'])
                items.append(user)
        
        return items

    def delete(self, email):
        try:
            db = Database(self.json_url)
            json_data = db.load_data()
                                                             
            for i in range(len(json_data)):
                if json_data[i]["email"] == email:
                    json_data.pop(i)
                    db.save_data(json_data)
                    return True

            return False
        except BaseException:
            print('Error, ha ocurrido un error eliminando el usuario.')

    def find(self, email):
        db = Database(self.json_url)
        json_data = db.load_data()
        for item in json_data:
            if item['email'] == email:
                return item
        return None
    
    def store(self, user):
        try:
            data = {
                "age": user.age, 
                "email": user.email, 
                "names": user.names, 
                "surnames": user.surnames
            }

            db = Database(self.json_url)
            json_data = db.load_data()
            json_data.append(data)
            db.save_data(json_data)
            return True
        except:
            return False

    def update(self, user, email):
        try:
            data = {
                "age": user.age, 
                "email": user.email, 
                "names": user.names, 
                "surnames": user.surnames
            }

            db = Database(self.json_url)
            json_data = db.load_data()
            for i in range(len(json_data)):
                if json_data[i]["email"] == email:
                    json_data[i] = data
                    db.save_data(json_data)
                    return True
            
            return False
        except:
            return False
