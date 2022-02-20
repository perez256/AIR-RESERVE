import pdb
from api.tests.test_setup import TestSetUp


# list flights test
class TestFlight(TestSetUp):
    def test_flights_can_be_retrieved(self):
        res = self.client.get(self.flights_url)
        pdb.set_trace()
        self.assertEqual(res.status_code, 200)

    def test_cannot_access_bookings_unless_authenticated(self):
        res = self.client.get(self.bookings_url)
        pdb.set_trace()
        self.assertEqual(res.status_code, 401)




