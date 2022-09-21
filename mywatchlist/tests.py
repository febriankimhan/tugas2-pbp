from django.test import TestCase, Client

# Create your tests here.
class MyWatchListTest(TestCase):
    def test_mywatchlist_url_exists(self):
        for format in ['html', 'xml', 'json']:
            response = Client().get(f'/mywatchlist/{format}/')
            self.assertEqual(response.status_code, 200)