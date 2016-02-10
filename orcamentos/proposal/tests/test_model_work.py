from datetime import datetime
from django.shortcuts import resolve_url as r
from django.test import TestCase
from orcamentos.crm.models import Person, Customer, Occupation
from orcamentos.proposal.models import Work
from orcamentos.crm.tests.data import PERSON_DICT, CUSTOMER_DICT
from orcamentos.proposal.tests.data import WORK_DICT


class WorkTest(TestCase):

    def setUp(self):
        self.occupation = Occupation.objects.create(occupation='Gerente')

        self.person = Person.objects.create(
            occupation=self.occupation, **PERSON_DICT)

        self.customer = Customer.objects.create(**CUSTOMER_DICT)

        self.obj = Work.objects.create(
            person=self.person,
            customer=self.customer,
            **WORK_DICT)

    def test_create(self):
        self.assertTrue(Work.objects.exists())

    def test_str(self):
        self.assertEqual('Ed. Atlanta', str(self.obj))

    def test_ordering(self):
        self.assertListEqual(['name_work'], Work._meta.ordering)

    def test_get_absolute_url(self):
        url = r('proposal:work_detail', slug=self.obj.slug)
        self.assertEqual(url, self.obj.get_absolute_url())
