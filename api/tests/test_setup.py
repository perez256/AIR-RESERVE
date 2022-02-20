from rest_framework.test import APITestCase
from django.urls import reverse


class TestSetUp(APITestCase):
    def setUp(self):
        self.register_url = reverse('signup')
        self.login_url = reverse('token_obtain_pair')

        self.flights_url = reverse('flights')
        self.bookings_url = reverse('bookings')
        self.create_booking_url = reverse('create_booking')

        # create user
        self.user_data = {
            "username": "dst25",
            "password": "admin@123",
            "email": "ttsrr@gmail.com",
            "first_name": "Kato",
            "last_name": "John"
        }

        self.create_booking_data = {
            "_id": 2,
            "date_reserve": None,
            "date_cancel": None,
            "is_canceled": "false",
            "user": 1,
            "ticket": 1
        }
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
