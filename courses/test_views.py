from django.test import TestCase
from .models import Course

# Create your tests here.


class TestViews(TestCase):

    def test_get_courses(self):
        response = self.client.get('/courses/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/courses.html')

    def test_get_course_details(self):
        course = Course.objects.create(course_name='Test course detail')
        response = self.client.get(f'/courses/{course.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/course_detail.html')

    def test_book_tee_time(self):
        response = self.client.post('courses/book/', {'course': 'Test add booking'})
        self.assertRedirects(response, 'paygreenfee')
