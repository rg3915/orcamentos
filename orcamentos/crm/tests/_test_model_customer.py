from datetime import datetime
from django.shortcuts import resolve_url as r
from django.test import TestCase
from orcamentos.crm.models import Customer
from .data import CUSTOMER_DICT


class CustomerTest(TestCase):

    def setUp(self):
        self.obj = Customer.objects.create(**CUSTOMER_DICT)

    def test_create(self):
        self.assertTrue(Customer.objects.exists())

    def test_created(self):
        ''' Customer must have an auto created attr. '''
        self.assertIsInstance(self.obj.created, datetime)

    def test_str(self):
        self.assertEqual('Arq. Mike Smith', str(self.obj))

    def test_ordering(self):
        self.assertListEqual(['first_name'], Customer._meta.ordering)

    def test_get_absolute_url(self):
        url = r('crm:customer_detail', slug=self.obj.slug)
        self.assertEqual(url, self.obj.get_absolute_url())
