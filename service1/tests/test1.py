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