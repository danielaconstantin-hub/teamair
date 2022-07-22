from flask import url_for
from unittest.mock import patch
#from unittest.mock import mock
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app


class TestRandom(TestBase):
    def test_get_numbers(self):
        with patch('random.randint') as r:
            r.return_value = 0
            response = self.client.get(url_for('get_numbers'))
            self.assertIn(b'1', response.data)
        with patch('random.randint') as r:
            r.return_value = 1
            response = self.client.get(url_for('get_numbers'))
            self.assertIn(b'2', response.data)
        with patch('random.randint') as r:
            r.return_value = 2
            response = self.client.get(url_for('get_numbers'))
            self.assertIn(b'3', response.data)
        with patch('random.randint') as r:
            r.return_value = 3
            response = self.client.get(url_for('get_numbers'))
            self.assertIn(b'4', response.data)

        with patch('random.randint') as r:
            r.return_value = 4
            response = self.client.get(url_for('get_numbers'))
            self.assertIn(b'5', response.data)

        with patch('random.randint') as r:
            r.return_value = 5
            response = self.client.get(url_for('get_numbers'))
            self.assertIn(b'6', response.data)

        with patch('random.randint') as r:
            r.return_value = 6
            response = self.client.get(url_for('get_numbers'))
            self.assertIn(b'7', response.data)

        with patch('random.randint') as r:
            r.return_value = 7
            response = self.client.get(url_for('get_numbers'))
            self.assertIn(b'8', response.data)

        with patch('random.randint') as r:
            r.return_value = 8
            response = self.client.get(url_for('get_numbers'))
            self.assertIn(b'9', response.data)

        with patch('random.randint') as r:
            r.return_value = 9
            response = self.client.get(url_for('get_numbers'))
            self.assertIn(b'10', response.data)