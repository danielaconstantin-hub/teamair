from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase



import requests_mock
import pytest

class TestBase(TestCase):
    def create_app(self):
        return app

class TestRandom(TestBase):
    def test_get_letter(self):
        with patch('random.randint') as r:
            r.return_value = 0
            response = self.client.get(url_for('/get/letters'))
            self.assertIn(b'a', response.data)
        with patch('random.randint') as r:
            r.return_value = 1
            response = self.client.get(url_for('/get/letters'))
            self.assertIn(b'b', response.data)
        with patch('random.randint') as r:
            r.return_value = 2
            response = self.client.get(url_for('/get/letters'))
            self.assertIn(b'c', response.data)
        with patch('random.randint') as r:
            r.return_value = 3
            response = self.client.get(url_for('/get/letters'))
            self.assertIn(b'd', response.data)

        with patch('random.randint') as r:
            r.return_value = 4
            response = self.client.get(url_for('/get/letters'))
            self.assertIn(b'e', response.data)

        with patch('random.randint') as r:
            r.return_value = 5
            response = self.client.get(url_for('/get/letters'))
            self.assertIn(b'f', response.data)

        with patch('random.randint') as r:
            r.return_value = 6
            response = self.client.get(url_for('/get/letters'))
            self.assertIn(b'g', response.data)

        with patch('random.randint') as r:
            r.return_value = 7
            response = self.client.get(url_for('/get/letters'))
            self.assertIn(b'h', response.data)

        with patch('random.randint') as r:
            r.return_value = 8
            response = self.client.get(url_for('/get/letters'))
            self.assertIn(b'i', response.data)

        with patch('random.randint') as r:
            r.return_value = 9
            response = self.client.get(url_for('/get/letters'))
            self.assertIn(b'j', response.data)