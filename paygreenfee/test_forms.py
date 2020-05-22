from django.test import TestCase
from .forms import PaymentInfoForm


class TestUserPaymentInfoForm(TestCase):

    def all_fields_correct(self):
        form = PaymentInfoForm({'first_name': 'test',
                                'last_name': 'test',
                                'email': 'test@test.com',
                                'phone_number': '2347547458'})
        self.assertTrue(form.is_valid())

    def all_fields_required(self):
        form = PaymentInfoForm({'first_name': '',
                                'last_name': '',
                                'email': '',
                                'phone_number': ''})
        self.assertFalse(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = PaymentInfoForm()
        self.assertEqual(form.Meta.fields, ('first_name', 'last_name',
                                            'email', 'phone_number'))
