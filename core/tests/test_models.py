from django.test import TestCase
from django.db import IntegrityError
from datetime import datetime
from core.models import Person
from core.models import Customer
from core.models import Employee
from core.models import Occupation
from core.models import Seller
from core.models import Entry
from core.models import Category
from core.models import Work
from core.models import Proposal
from core.models import NumLastProposal


class PersonTest(TestCase):

    def setUp(self):
        self.occupation = Occupation.objects.create(
            occupation=u'Orçamentista'
        )
        self.obj = Person(
            gender='M',
            treatment='sr',
            first_name='Regis',
            last_name='da Silva',
            company='Acme',
            department=u'Orçamentos',
            occupation=self.occupation,
            email='regis@example.com',
            phone1='7543-2101',
            phone2='7543-2102',
            phone3='7543-2103',
            cpf='11122233396',
            rg='40373800',
            address=u'Avenida Paulista, 1320',
            complement='Apto 303',
            district=u'Cerqueira César',
            city=u'São Paulo',
            uf='SP',
            cep='01020000',
            active=True
        )
        # CPF válido: 33322211169, 55566678963

    def test_create(self):
        self.obj.save()
        self.assertEqual(1, self.obj.pk)

    def test_has_created_at(self):
        'Person must have automatic created'
        self.obj.save()
        self.assertIsInstance(self.obj.created, datetime)


class CustomerTest(TestCase):

    def setUp(self):
        self.obj = Person(
            gender='M',
            treatment='sr',
            first_name='Adailton',
            last_name='do nascimento',
            company='Acme',
            department=u'Developer',
            email='dhelbegors@example.com',
            phone1='7543-2101',
            phone2='7543-2102',
            phone3='7543-2103',
            cpf='11122233396',
            rg='40373800',
            address=u'Rua rafael barbosa',
            complement='SC',
            district=u'Cerqueira César',
            city=u'Goiás',
            uf='GO',
            cep='01020000',
            cnpj='00194604000116',
            ie='1110125462',
            type_customer='a',
            active=True,
        )

    def test_create(self):
        self.obj.save()
        self.assertEqual(1, self.obj.pk)

    def test_has_created_at(self):
        'Person must have automatic created'
        self.obj.save()
        self.assertIsInstance(self.obj.created, datetime)


class EmployeeTest(TestCase):
    pass


class NumLastProposalTest(TestCase):
    pass


class ProposalTest(TestCase):
    pass


class WorkTest(TestCase):
    pass


class CategoryTest(TestCase):
    pass


class EntryTest(TestCase):
    pass


class SellerTest(TestCase):
    pass


class OccupationTest(TestCase):
    pass


class PeopleTest(TestCase):
    pass


class AddressTest(TestCase):
    pass
