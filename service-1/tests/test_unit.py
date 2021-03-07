import unittest
from unittest.mock import patch
from flask import url_for, Response, request
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_service2(self):
        with patch("requests.get") as g:
            g.return_value.text = "whiskey"
            response = self.client.get(url_for("index"))
            self.assertEqual(response.status_code,200)
            self.assertIn(b"whiskey", response.data)

    def test_service3(self):
        with patch("requests.get") as g:
            g.return_value.text = "redbull"
            response = self.client.get(url_for("index"))
            self.assertEqual(response.status_code,200)
            self.assertIn(b"redbull", response.data)