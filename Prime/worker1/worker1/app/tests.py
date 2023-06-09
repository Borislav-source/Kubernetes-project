from django.test import TestCase, Client
from django.urls import reverse
from django.http import HttpRequest
from worker1.app.views import my_view


# Create your tests here.
class MyViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_my_view_with_valid_data(self):
        url = reverse('my_view')
        response = self.client.get(url, {'num': '2'})

        self.assertEqual(response.status_code, 200)


    def test_my_view_with_invalid_data(self):
        url = reverse('my_view')
        response = self.client.get(url, {'num': '40'})

        self.assertEqual(response.status_code, 500)
