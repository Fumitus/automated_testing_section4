from unittest import TestCase
from app import app
import json


class TestHome(TestCase):
    def test_home(self):
        with app.app.test_client() as c:
            resp = c.get('/')

            self.assertEqual(200, resp.status_code)
            self.assertEqual({'message': "Hello world!"}, json.loads(resp.get_data()))
