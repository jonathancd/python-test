import unittest
from src.Validations.UserValidator import UserValidator
from src.Models.User import User

class TestUserDao(unittest.TestCase):

    def test_data_good_all(self):
        names = 'Test'
        surnames = 'Test'
        age = 30
        email = 'user@email.com'
        result = UserValidator.validateData(names, surnames, age, email)
        self.assertEqual(len(result), 0)

    def test_data_bad_age(self):
        names = 'Test'
        surnames = 'Test'
        age = -1
        email = 'user@email.com'
        result = UserValidator.validateData(names, surnames, age, email)
        self.assertEqual(len(result), 1)

    def test_data_bad_email(self):
        names = 'Test'
        surnames = 'Test'
        age = 30
        email = 'useremail.com'
        result = UserValidator.validateData(names, surnames, age, email)
        self.assertEqual(len(result), 1)

    def test_data_bad_names(self):
        names = 'T'
        surnames = 'Test'
        age = 30
        email = 'user@email.com'
        result = UserValidator.validateData(names, surnames, age, email)
        self.assertEqual(len(result), 1)

    def test_data_bad_surnames(self):
        names = 'Tes'
        surnames = 'T'
        age = 30
        email = 'user@email.com'
        result = UserValidator.validateData(names, surnames, age, email)
        self.assertEqual(len(result), 1)

    def test_data_bad_all(self):
        names = 'T'
        surnames = 'T'
        age = 500
        email = 'useremail.com'
        result = UserValidator.validateData(names, surnames, age, email)
        self.assertEqual(len(result), 4)


if __name__ == '__main__':
    unittest.main()