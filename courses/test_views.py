from django.test import TestCase
from .models import Course, TeeTime
from golfprofile.models import User
from paygreenfee.models import TeeTimePurchase, PaymentInfo
# Create your tests here.


class TestViews(TestCase):

    def setUp(self):
        self.test_user = User.objects.create_user(
            username='testlogin',
            email='tester123@testing.com',
            password='thisisatest123')

    def tearDown(self):
        User.objects.all().delete()

    def test_get_courses(self):
        response = self.client.get('/courses/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/courses.html')

    def test_get_course_details(self):
        course = Course.objects.create(course_name='Test course detail')
        response = self.client.get(f'/courses/{course.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/course_detail.html')

    def test_create_tee_time_and_add_to_bag(self):
        self.client.login(username='testlogin', password='thisisatest123')
        course_bag = {}
        self.test_course = Course.objects.create(
                            course_name='test course',
                            green_fee=200,
        )
        teetime = TeeTime.objects.create(course=self.test_course,
                                         tee_time='2020-06-06 13:30',
                                         booked=False, player=self.test_user.userprofile)
        print(teetime)
        course_bag[self.test_course.id] = [teetime.id]
        response = self.client.post('book/', course_bag)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/courses.html')

