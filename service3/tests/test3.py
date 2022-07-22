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
    def test_5