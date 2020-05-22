from django.test import TestCase
from .models import TeeTime, Course
from golfprofile.models import User
# Create your tests here.


class TestModels(TestCase):

    def test_booked_defaults_to_true(self):
        self.test_user = User.objects.create_user(
            username='testlogin',
            email='tester123@testing.com',
            password='thisisatest123')
        self.test_course = Course.objects.create(
            course_name='test course'
        )
        teetime = TeeTime.objects.create(course=self.test_course,
                                         tee_time='2020-06-06 13:30',
                                         booked=True, player=self.test_user.userprofile)
        self.assertTrue(teetime.booked)
