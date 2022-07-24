from django.contrib.auth import get_user_model
from django.test import TestCase


class AccountsTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': '09123456789',
            'email': 'test@email.com',
            'password': 'secret', }
        get_user_model().objects.create_user(**self.credentials)

    def test_login(self):
        response = self.client.login(
            username='09123456789', password='secret',)
        self.assertTrue(response, True)
