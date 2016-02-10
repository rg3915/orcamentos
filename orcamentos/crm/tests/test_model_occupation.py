from django.test import TestCase
from orcamentos.crm.models import Occupation


class OccupationTest(TestCase):

    def setUp(self):
        self.obj = Occupation.objects.create(occupation='Gerente')

    def test_create(self):
        self.assertTrue(Occupation.objects.exists())

    def test_str(self):
        self.assertEqual('Gerente', str(self.obj))
