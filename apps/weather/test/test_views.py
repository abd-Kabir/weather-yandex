from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class MyViewTests(APITestCase):
    def test_weather_view(self):
        url = reverse('weather:weather_by_city')  # Replace with your actual view name
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
