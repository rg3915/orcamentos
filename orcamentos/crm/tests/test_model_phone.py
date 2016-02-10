from django.test import TestCase
from orcamentos.crm.models import Phone, Person
from .data import PERSON_DICT


class PhoneTest(TestCase):

    def setUp(self):
        self.person = Person.objects.create(**PERSON_DICT)

    def test_create(self):
        phone = Phone.objects.create(
            phone='11 98765-4321',
            person=self.person,
            phone_type='pri')
        self.assertTrue(Phone.objects.exists())
