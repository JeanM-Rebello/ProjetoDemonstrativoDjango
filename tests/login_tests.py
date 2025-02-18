from django.test import TestCase
from django.urls import reverse

class LoginTest(TestCase):
    def test_login_page_load(self):
        response = self.client.get(reverse('accounts:login'))
        self.assertEqual(response.status_code, 200)