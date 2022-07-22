from flask import url_for
from flask_testing import TestCase
from requests_mock import mock

from app import app, db


class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_get_letter(self):
        