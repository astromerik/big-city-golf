from django.test import TestCase
from .models import UserProfile


class TestModels(TestCase):

    def create_user_profile(self):
        user = UserProfile.objects.create({'town': 'test'})
        self.assertTrue(UserProfile.test)