from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResult(TestBase):
    def test_num(self):
        with patch('requests.get') as n:
            n.return_value.text = '5'

            response = self.client.get(url_for('get_numbers'))
            self.assertIn(b'5', response.data)
            