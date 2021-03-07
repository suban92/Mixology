import unittest
from unittest.mock import patch
from flask import url_for, Response, request
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestService2(TestBase):
    def test_spirit(self):
        with patch("random.randrange") as r:
            r.return_value = 5
            response = self.client.get(url_for("spirit"))
            self.assertIn(b"Tequila", response.data)
