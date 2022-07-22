from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app
import requests
import requests_mock
import pytest

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_5_and_a(self):
        with requests_mock.Mocker() as m:
            with patch('requests.post') as p:
                m.get('http://localhost:5001/get/numbers', text='5')
                m.get('http://localhost:5002/get/letters', text='a')
                p.return_value.text= '5 and a'
                response= self.client.get(url_for('get_num_let'))
                self.assertIn(b'5 a', response.data)
                self.assertIn(b'5 and a', response.data)