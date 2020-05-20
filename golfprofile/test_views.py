from django.test import TestCase
from django.contrib.auth.models import User
from courses.models import TeeTime
from golfprofile.models import UserProfile


class TestViews(TestCase):

    def setUp(self):
        self.test_user = User.objects.create_user(
            username='testlogin',
            email='tester123@testing.com',
            password='thisisatest123')
        print('setUp')
        print([u for u in User.objects.all()])
        print([u for u in UserProfile.objects.all()])

    def tearDown(self):
        User.objects.all().delete()
        print('tearDown')
        print([u for u in User.objects.all()])
        print([u for u in UserProfile.objects.all()])

    def test_get_golfprofile_when_logged_in(self):
        self.client.login(username='testlogin', password='thisisatest123')
        response = self.client.get("/golfprofile/", follow=True)
        self.assertEqual(response.status_code, 200)

    def test_get_golfprofile_when_not_logged_in(self):
        response = self.client.get("/golfprofile/")
        self.assertEqual(response.status_code, 302)

    def test_delete_tee_time(self):
        self.client.login(username='testlogin', password='thisisatest123')
        tee_time = TeeTime.objects.create(course_id='1',
                                          tee_time='2020-06-06 13:30',
                                          price=200, booked=True,
                                          player=self.test_user.userprofile)
        response = self.client.get(f"/delete_tee_time/{tee_time.id}")
        self.assertRedirects(response, "/golfprofile/")

