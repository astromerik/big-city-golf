from django.test import TestCase
from .models import TeeTime
# Create your tests here.


class TestModels(TestCase):

    def test_booked_defaults_to_true(self):
        teetime = TeeTime.objects.create(tee_time='2020-09-09 08:00')
        self.assertTrue(teetime.booked)