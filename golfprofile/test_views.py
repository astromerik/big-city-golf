from django.test import TestCase
from django.contrib.auth.models import User
from courses.models import TeeTime, Course
from paygreenfee.models import PaymentInfo, TeeTimePurchase
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
        self.test_course = Course.objects.create(
                            course_name='test course',
                            green_fee=200,
        )
        teetime = TeeTime.objects.create(course=self.test_course,
                                         tee_time='2020-06-06 13:30',
                                         booked=True, player=self.test_user.userprofile)
        testpurchase = PaymentInfo.objects.create(
            order_number='12345',
            first_name='test',
            last_name='test',
            email='test@test.com',
            phone_number='123123442',
            purchase_date='2020-06-06 13:37',
            total_greenfee=1600,
            stripe_pid='12312343'
        )
        tee_time = TeeTimePurchase.objects.create(payment_info=testpurchase,
                                          tee_time=teetime,
                                          greenfee=self.test_course.green_fee,
                                          course=self.test_course)
        response = self.client.get(f"/remove/{tee_time.id}")
        

