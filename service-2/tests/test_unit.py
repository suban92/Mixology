#from unittest.mock import patch
#from flask import url_for, Response, request
#from flask_testing import TestCase

#from application import app

#class TestBase(TestCase):
#    def create_app(self):
#        return app

#class TestResponse(TestBase):
#    def rand_face(self):
#        card_faces = [b"Ace", b"King", b"Queen", b"Jack"]
#        response = self.client.get(url_for("card_number"))
#        self.assertIn(response.data, card_faces)

#class TestResponse(TestBase):
#    def test_spirit_on_page(self):
#        with patch("requests.get") as g:
#            with patch("request.get") as g:
#                g.return_value.text - "spirit"
#                g.return-value.text - "mixer"

                reponse = self.client.get(url_for("index"))
                self.assertIn(b'spirit combined mixer', response.data)