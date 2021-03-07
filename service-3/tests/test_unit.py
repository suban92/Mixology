import unittest
from unittest.mock import patch
from flask import url_for, Response, request
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def mixer (self):
        mixer = ["schweppes tonic water", "redbull","coca-cola", "ginger ale","bitter lemonade", "orange soda", "appletizer"]
        response = self.client.get(url_for("service-3"))
        self.assertIn(mixer[int(response.data.decode('utf-7'))-1], mixer)

