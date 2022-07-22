from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

import requests_mock
import pytest

class TestBase(TestCase):
    def create_app(self):
        return app

class TestRandom(TestBase):
    def test_5_and_a(self):
        response = self.client.post(url_for('get_result'), data='5 a')
        self.assertIn(b'5 and a', response.data)

    def test_else(self):
        response= self.client.post(url_for('get_result'), data='1 g')
        self.assertIn(b'other', response.data)