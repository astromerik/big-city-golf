from django.test import TestCase
from .models import TeeTime
# Create your tests here.


class TestModels(TestCase):

    def test_booked_defaults_to_true(self):
        teetime = TeeTime.objects.create(course_id='1', tee_time='2020-06-06 13:30',
                                         price=200, booked=True, player=1)
        self.assertTrue(teetime.booked)