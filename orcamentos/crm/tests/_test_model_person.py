from datetime import datetime
from django.shortcuts import resolve_url as r
from django.test import TestCase
from orcamentos.crm.models import Person, Occupation
from .data import PERSON_DICT


class PersonTest(TestCase):

    def setUp(self):
        self.occupation = Occupation.objects.create(occupation='Gerente')
        self.obj = Person.objects.create(
            occupation=self.occupation, **PERSON_DICT)

    def test_create(self):
        self.assertTrue(Person.objects.exists())

    def test_created(self):
        ''' Person must have an auto created attr. '''
        self.assertIsInstance(self.obj.created, datetime)

    def test_str(self):
        self.assertEqual('Sr. Regis da Silva', str(self.obj))

    def test_ordering(self):
        self.assertListEqual(['first_name'], Person._meta.ordering)

    def test_get_absolute_url(self):
        url = r('crm:person_detail', slug=self.obj.slug)
        self.assertEqual(url, self.obj.get_absolute_url())
