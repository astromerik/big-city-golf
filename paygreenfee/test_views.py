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

    def test_get_paygreenfee(self):
        self.client.login(username='testlogin', password='thisisatest123')
        stripe_secret_key = settings.STRIPE_SECRET_KEY
        stripe.api_key = stripe_secret_key
        stripe.PaymentIntent.create(
            amount=5550,
            currency=settings.STRIPE_CURRENCY,
        )
        response = self.client.get("/paygreenfee/")
        self.assertEqual(response.status_code, 200)
