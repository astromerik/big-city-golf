from django.test import TestCase
from django.contrib.auth.models import User
from courses.models import TeeTime
from golfprofile.models import UserProfile

class TestViews(TestCase):

    def test_get_golfprofile_when_logged_in(self):
        User.objects.create_user(
            username='testlogin',
            email='tester123@testing.com',
            password='thisisatest123')
        self.client.login(username='testlogin', password='thisisatest123')
        response = self.client.get("/golfprofile/")
        self.assertEqual(response.status_code, 200)

    def test_get_golfprofile_when_not_logged_in(self):
        response = self.client.get("/golfprofile/")
        self.assertEqual(response.status_code, 302)

    def test_delete_tee_time(self):
        User.objects.create_user(
            username='testlogin',
            email='tester123@testing.com',
            password='thisisatest123')
        UserProfile.objects.create(
            user=User.username
        )
        self.client.login(username='testlogin', password='thisisatest123')
        tee_time = TeeTime.objects.create(course_id='1', tee_time='2020-06-06 13:30',
                                         price=200, booked=True, player=Userprofile.user)
        response = self.client.get(f"/delete_tee_time/{tee_time.id}")
        self.assertRedirects(response, "/golfprofile/")
        existing_tee_time = TeeTime.objects.filter(id=tee_time.id)
        self.assertEqual(len(existing_tee_time),0)
