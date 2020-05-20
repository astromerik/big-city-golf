from django.test import TestCase
from .forms import UserProfileForm


class TestUserProfileForm(TestCase):

    def test_fields_are_not_required(self):
        form = UserProfileForm({'town': ''})
        self.assertTrue(form.is_valid())

    def test_phone_number_is_required_to_be_a_phonenumber_field(self):
        form = UserProfileForm({'phone_number': '3212312312'})
        self.assertFalse(form.is_valid())
    
    def test_phonenumber_field_correct_input(self):
        form = UserProfileForm({'phone_number': '+4612341234'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = UserProfileForm()
        self.assertEqual(form.Meta.fields, ['phone_number', 'address',
                                            'town', 'golf_id', 'handicap'])
