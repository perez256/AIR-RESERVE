from api.tests.test_setup import TestSetUp
import pdb


# python manage.py test
# res.data

class TestAuthenticate(TestSetUp):
    # test if user cant login with no data [res]
    def test_user_cannot_signup_with_no_data(self):
        res = self.client.post(self.register_url)
        pdb.set_trace()
        self.assertEqual(res.status_code, 400)

    def test_user_can_signup_correctly(self):
        res = self.client.post(self.register_url, format="json")
        pdb.set_trace()
        self.assertEqual(res.status_code, 201)
