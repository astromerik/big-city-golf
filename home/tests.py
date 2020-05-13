from django.test import TestCase

# Create your tests here.

class TestDjango(TestCase):

    # Test that the home page loads propperly
    # and that all paths work
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)