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
            with patch('requests.post') as p:
                p.return_value.text = 'b'
                n.return_value.text = '4'

                response = self.client.get(url_for('get_num_let'))
                self.assertIn(b'4', response.data)
                self.assertIn(b'b', response.data)