from django.test import TestCase, Client

# Create your tests here.
class AppTest(TestCase):
    def test_app_html(self):
        response = Client().get('https://andretugas2pbp.herokuapp.com/mywatchlist/html/')
        self.assertEqual(response.status_code,200)

    def test_app_xml(self):
        response = Client().get('https://andretugas2pbp.herokuapp.com/mywatchlist/xml/')
        self.assertEqual(response.status_code,200)

    def test_app_json(self):
        response = Client().get('https://andretugas2pbp.herokuapp.com/mywatchlist/json/')
        self.assertEqual(response.status_code,200)
