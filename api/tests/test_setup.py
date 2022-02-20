from rest_framework.test import APITestCase
from django.urls import reverse


class TestSetUp(APITestCase):
    def setUp(self):
        self.register_url = reverse('signup')
        self.login_url = reverse('token_obtain_pair')

        self.flights_url = reverse('flights')
        self.bookings_url = reverse('bookings')

        # create user
        self.idx = 1
        self.user_data = {
            "username": "dst25",
            "password": "admin@123",
            "email": "ttsrr@gmail.com",
            "first_name": "Kato",
            "last_name": "John"
        }
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
