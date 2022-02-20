import pdb
from api.tests.test_setup import TestSetUp


# list flights test
class TestFlight(TestSetUp):
    # all flights
    def test_flights_can_be_retrieved(self):
        res = self.client.get(self.flights_url)
        pdb.set_trace()
        self.assertEqual(res.status_code, 200)

    # only authenticated users
    def test_cannot_access_bookings_unless_authenticated(self):
        res = self.client.get(self.bookings_url)
        pdb.set_trace()
        self.assertEqual(res.status_code, 401)

    # Create booking
    def test_user_can_create_booking(self):
        res = self.client.post(self.create_booking_url, format="json")
        pdb.set_trace()
        self.assertEqual(res.status_code, 201)
