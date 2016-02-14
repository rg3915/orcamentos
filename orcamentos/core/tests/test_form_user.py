from django.contrib.auth.models import User
from django.shortcuts import resolve_url as r
from django.test import TestCase
from orcamentos.core.forms import UserForm


class UserFormTest(TestCase):

    def test_form_has_fields(self):
        ''' Form must have 3 fields '''
        form = UserForm()
        expected = ['username', 'email', 'password']
        self.assertSequenceEqual(expected, list(form.fields))
