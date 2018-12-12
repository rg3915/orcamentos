from datetime import datetime
from django.test import TestCase
from django.contrib.auth.models import User
from orcamentos.crm.models import Employee, Occupation
from .data import USER_DICT, EMPLOYEE_DICT


class EmployeeTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(**USER_DICT)
        self.occupation = Occupation.objects.create(occupation='Gerente')
        self.obj = Employee.objects.create(user=self.user, **EMPLOYEE_DICT)

    def test_create(self):
        self.assertTrue(Employee.objects.exists())

    def test_created(self):
        ''' Employee must have an auto created attr. '''
        self.assertIsInstance(self.obj.created, datetime)

    def test_str(self):
        self.assertEqual('regis', str(self.obj))

    def test_ordering(self):
        self.assertListEqual(['user__first_name'], Employee._meta.ordering)
