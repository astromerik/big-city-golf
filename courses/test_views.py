from django.test import TestCase
from .models import Course
from golfprofile.models import User
from .models import TeeTime
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

    def test_add_to_course_bag(self):
        self.client.login(username='testlogin', password='thisisatest123')
        response = self.client.post('book/', [('2020-06-06 13:30', 1500, 'Barsebäck G&CC')])
        self.assertRedirects(response, 'paygreenfee/')

