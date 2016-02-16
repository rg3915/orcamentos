from datetime import datetime
from django.test import TestCase
from django.contrib.auth.models import User
from orcamentos.crm.models import Employee, Occupation
from .data import USER_DICT, EMPLOYEE_DICT


class EmployeeTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='abel',
            first_name='Abel',
            last_name='Lima',
            email='abel@example.com',
            password='wplysntw',)
        self.occupation = Occupation.objects.create(occupation='Gerente')
        self.obj = Employee.objects.get(user=self.user)

    def test_create(self):
        self.assertTrue(Employee.objects.exists())

    def test_created(self):
        ''' Employee must have an auto created attr. '''
        self.assertIsInstance(self.obj.created, datetime)

    def test_date_entry(self):
        ''' Employee must have an auto date_entry attr. '''
        self.assertIsInstance(self.obj.date_entry, datetime)

    def test_date_release(self):
        ''' Employee must have an auto date_release attr. '''
        self.assertIsInstance(self.obj.date_release, datetime)

    def test_str(self):
        self.assertEqual('regis', str(self.obj))

    def test_ordering(self):
        self.assertListEqual(['user__first_name'], Employee._meta.ordering)
