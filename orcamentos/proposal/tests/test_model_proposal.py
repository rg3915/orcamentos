from datetime import datetime
from django.shortcuts import resolve_url as r
from django.test import TestCase
from django.contrib.auth.models import User
from orcamentos.crm.models import Person, Customer, Employee, Occupation, Seller
from orcamentos.proposal.models import Entry, Work, Proposal
from orcamentos.crm.tests.data import USER_DICT, PERSON_DICT, CUSTOMER_DICT, EMPLOYEE_DICT, SELLER_DICT
from orcamentos.proposal.tests.data import ENTRY_DICT, WORK_DICT, PROPOSAL_DICT


class ProposalTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(**USER_DICT)

        self.occupation = Occupation.objects.create(occupation='Gerente')

        self.person = Person.objects.create(
            occupation=self.occupation, **PERSON_DICT)

        self.customer = Customer.objects.create(**CUSTOMER_DICT)

        self.employee = Employee.objects.create(
            user=self.user,
            occupation=self.occupation,
            **EMPLOYEE_DICT)

        self.seller = Seller.objects.create(
            employee=self.employee, **SELLER_DICT)

        self.work = Work.objects.create(
            person=self.person,
            customer=self.customer,
            **WORK_DICT)

        self.obj = Proposal.objects.create(
            work=self.work,
            person=self.person,
            employee=self.employee,
            seller=self.seller,
            **PROPOSAL_DICT)

    def test_create(self):
        self.assertTrue(Proposal.objects.exists())

    def test_created(self):
        ''' Proposal must have an auto created attr. '''
        self.assertIsInstance(self.obj.created, datetime)

    def test_str(self):
        # Format expected 001.15.0
        actual_year = datetime.now().strftime('%y')
        self.assertEqual('001.{}.0'.format(actual_year), str(self.obj))

    def test_ordering(self):
        self.assertListEqual(['id'], Proposal._meta.ordering)

    def test_get_absolute_url(self):
        url = r('proposal:proposal_detail', pk=self.obj.pk)
        self.assertEqual(url, self.obj.get_absolute_url())
