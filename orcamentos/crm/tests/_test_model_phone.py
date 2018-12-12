from django.test import TestCase
from orcamentos.crm.models import Phone, Person
from .data import PERSON_DICT


class PhoneTest(TestCase):

    def setUp(self):
        self.person = Person.objects.create(**PERSON_DICT)
        phone = Phone(
            phone='11 98765-4321',
            person=self.person,
            phone_type='pri')
        phone.save()

    def test_create(self):
        self.assertTrue(Phone.objects.exists())
