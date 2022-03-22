class User():
    def __init__(self, age = None, email = None, names = None, surnames = None):
        self._age = age
        self._email = email
        self._names = names
        self._surnames = surnames

    @property
    def names(self):
        return self._names

    @property
    def surnames(self):
        return self._surnames
    
    @property
    def age(self):
        return self._age

    @property
    def email(self):
        return self._email

    @names.setter
    def names(self , names):
        self._names = names
 
    @surnames.setter
    def surnames(self , surnames):
        self._surnames = surnames

    @age.setter
    def age(self , age):
        self._age = age

    @email.setter
    def email(self , email):
        self._email = email
