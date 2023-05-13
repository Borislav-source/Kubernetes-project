from django.test import TestCase, Client
from django.urls import reverse


# Create your tests here.
class MyViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_my_view_with_valid_data(self):
        url = reverse('fibonacci_resolver')
        response = self.client.get(url, {'num': '5'})

        self.assertEqual(response.status_code, 200)

    def test_my_view_with_invalid_data(self):
        url = reverse('fibonacci_resolver')
        response = self.client.get(url, {'num': '9'})

        self.assertEqual(response.status_code, 500)
