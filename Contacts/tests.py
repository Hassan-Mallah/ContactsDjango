from django.test import SimpleTestCase
from . import views
from django.urls import reverse, resolve

# Create your tests here.


class TestUrls(SimpleTestCase):
    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, views.home)
