from django.test import TestCase
from django.contrib.auth.models import User
from orcamentos.crm.models import Employee, Occupation, Seller
from .data import USER_DICT, EMPLOYEE_DICT, SELLER_DICT


class SellerTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(**USER_DICT)
        self.occupation = Occupation.objects.create(occupation='Gerente')
        self.employee = Employee.objects.get(user=self.user)
        self.obj = Seller.objects.create(employee=self.employee, **SELLER_DICT)

    def test_create(self):
        self.assertTrue(Seller.objects.exists())

    def test_str(self):
        self.assertEqual('regis', str(self.obj))

    def test_ordering(self):
        self.assertListEqual(
            ['employee__user__first_name'], Seller._meta.ordering)
