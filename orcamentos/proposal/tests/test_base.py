from django.test import TestCase
from django.contrib.auth.models import User
from orcamentos.crm.models import Person, Customer, Employee, Occupation, Seller
from orcamentos.proposal.models import Entry, Work, Proposal, Contract
from orcamentos.crm.tests.data import PERSON_DICT, CUSTOMER_DICT, EMPLOYEE_DICT, SELLER_DICT
from orcamentos.proposal.tests.data import ENTRY_DICT, WORK_DICT, PROPOSAL_DICT


class BaseEntryTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='regis',
            first_name='Regis',
            last_name='da Silva',
            email='regis@example.com',
            password='wpxysntq',)

        self.occupation = Occupation.objects.create(occupation='Gerente')

        self.person = Person.objects.create(
            occupation=self.occupation, **PERSON_DICT)

        self.customer = Customer.objects.create(**CUSTOMER_DICT)

        self.employee = Employee.objects.get(user=self.user)

        self.seller = Seller.objects.create(
            employee=self.employee, **SELLER_DICT)

        self.work = Work.objects.create(
            person=self.person,
            customer=self.customer,
            **WORK_DICT)

        self.obj = Entry.objects.create(
            work=self.work,
            person=self.person,
            seller=self.seller,
            **ENTRY_DICT)


class BaseProposalTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='daniel',
            first_name='Daniel',
            last_name='Sousa',
            email='daniel@example.com',
            password='pkwltxsa',)

        self.occupation = Occupation.objects.create(occupation='Gerente')

        self.person = Person.objects.create(
            occupation=self.occupation, **PERSON_DICT)

        self.customer = Customer.objects.create(**CUSTOMER_DICT)

        self.employee = Employee.objects.get(user=self.user)

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


class BaseContractTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='jose',
            first_name='Jose',
            last_name='Maria',
            email='jose@example.com',
            password='dklhgtmr',
        )

        self.occupation = Occupation.objects.create(occupation='Gerente')

        self.person = Person.objects.create(
            occupation=self.occupation, **PERSON_DICT)

        self.customer = Customer.objects.create(**CUSTOMER_DICT)

        self.employee = Employee.objects.get(user=self.user)

        self.seller = Seller.objects.create(
            employee=self.employee, **SELLER_DICT)

        self.work = Work.objects.create(
            person=self.person,
            customer=self.customer,
            **WORK_DICT)

        self.proposal = Proposal.objects.create(
            work=self.work,
            person=self.person,
            employee=self.employee,
            seller=self.seller,
            **PROPOSAL_DICT)

        self.obj = Contract.objects.create(
            proposal=self.proposal,
            contractor=self.customer,
            is_canceled=False,
        )


class BaseWorkTest(TestCase):

    def setUp(self):
        self.occupation = Occupation.objects.create(occupation='Gerente')

        self.person = Person.objects.create(
            occupation=self.occupation, **PERSON_DICT)

        self.customer = Customer.objects.create(**CUSTOMER_DICT)

        self.obj = Work.objects.create(
            person=self.person,
            customer=self.customer,
            **WORK_DICT)
