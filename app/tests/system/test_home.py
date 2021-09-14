from app.tests.system.base_test import BaseTest
import json


class TestHome(BaseTest):
    def test_home(self):
        with self.app() as c:
            resp = c.get('/')

            self.assertEqual(200, resp.status_code)
            self.assertEqual({'message': "Hello world!"}, json.loads(resp.get_data()))
