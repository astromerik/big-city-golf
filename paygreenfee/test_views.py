from django.test import TestCase
from .models import TeeTime
from golfprofile.models import User
import stripe
from django.conf import settings
# Create your tests here.

class TestViews(TestCase):

    def setUp(self):
        self.test_user = User.objects.create_user(
            username='testlogin',
            email='tester123@testing.com',
            password='thisisatest123')

    def tearDown(self):
        User.objects.all().delete()

