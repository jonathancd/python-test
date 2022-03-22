import unittest
from src.Dao.UserDAO import UserDAO
from src.Models.User import User

class TestUserDao(unittest.TestCase):

    def test_users_all(self):
        user_dao = UserDAO()
        user_dao.json_url = 'test/fixtures/test_users.json'
        users = user_dao.index()
        self.assertIsInstance(users, list)

    def test_users_create(self):
        user = User()
        user.age = 30
        user.email = 'test@test.com'
        user.names = 'test'
        user.surnames = 'test'

        user_dao = UserDAO()
        user_dao.json_url = 'test/fixtures/test_users.json'
        result = user_dao.store(user)
        self.assertEqual(result, True)

    def test_users_created_find_exists(self):
        email = 'user@email.com'
        user_dao = UserDAO()
        user_dao.json_url = 'test/fixtures/test_users.json'
        user = user_dao.find(email)
        self.assertIsInstance(user, dict)

    def test_users_created_update_user_exist(self):
        user = User(30, 'test@test.com', 'User', 'User')
        user_dao = UserDAO()
        user_dao.json_url = 'test/fixtures/test_users.json'
        result = user_dao.update(user, 'test@test.com')
        self.assertEqual(result, True)

    def test_users_find_non_exists(self):
        email = 'test@nonexists.com'
        user_dao = UserDAO()
        user_dao.json_url = 'test/fixtures/test_users.json'
        user = user_dao.find(email)
        self.assertEqual(user, None)

    def test_users_update_non_exist(self):
        user = User(30, 'test@test.com', 'User', 'User')
        user_dao = UserDAO()
        user_dao.json_url = 'test/fixtures/test_users.json'
        result = user_dao.update(user, 'test@not_email.com')
        self.assertEqual(result, False)

    def test_users_delete(self):
        user_dao = UserDAO()
        user_dao.json_url = 'test/fixtures/test_users.json'
        result = user_dao.delete('test@test.com')
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()