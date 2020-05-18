from django.test import TestCase
from .forms import TeeTimeForm
# Create your tests here.


class TestTeeTimeForm(TestCase):
    def test_tee_time_required(self):
        form = TeeTimeForm({'tee_time': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('tee_time', form.errors.keys())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = TeeTimeForm()
        self.assertEqual(form.Meta.fields, ['tee_time', 'course', 'price'])
