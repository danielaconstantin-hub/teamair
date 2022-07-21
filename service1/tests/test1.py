from flask import url_for
from flask_testing import TestCase
from requests_mock import mock

from app import app, db

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_home(self):

        with mock() as m:
            m.get('http://service2:5002/get/letters', text='')
            m.get('http://service3:5003/get/...', text='')
            m.post('http://service4:5004/post/...', json=12)

            response = self.client.get(url_for('home'))

        self.assert200(response)


class TestRandom(TestBase):
    def test_get_numbers(self):
        with patch('random.randint') as r:
            r.return_value = 0
            response = self.client.get(url_for('/get/numbers'))
            self.assertIn(b'1', response.data)
        with patch('random.randint') as r:
            r.return_value = 1
            response = self.client.get(url_for('/get/numbers'))
            self.assertIn(b'2', response.data)
        with patch('random.randint') as r:
            r.return_value = 2
            response = self.client.get(url_for('/get/numbers'))
            self.assertIn(b'3', response.data)
        with patch('random.randint') as r:
            r.return_value = 3
            response = self.client.get(url_for('/get/numbers'))
            self.assertIn(b'4', response.data)

        with patch('random.randint') as r:
            r.return_value = 4
            response = self.client.get(url_for('/get/numbers'))
            self.assertIn(b'5', response.data)

        with patch('random.randint') as r:
            r.return_value = 5
            response = self.client.get(url_for('/get/numbers'))
            self.assertIn(b'6', response.data)

        with patch('random.randint') as r:
            r.return_value = 6
            response = self.client.get(url_for('/get/numbers'))
            self.assertIn(b'7', response.data)

        with patch('random.randint') as r:
            r.return_value = 7
            response = self.client.get(url_for('/get/numbers'))
            self.assertIn(b'8', response.data)

        with patch('random.randint') as r:
            r.return_value = 8
            response = self.client.get(url_for('/get/numbers'))
            self.assertIn(b'9', response.data)

        with patch('random.randint') as r:
            r.return_value = 9
            response = self.client.get(url_for('/get/numbers'))
            self.assertIn(b'10', response.data)