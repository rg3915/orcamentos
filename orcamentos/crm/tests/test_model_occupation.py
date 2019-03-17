from django.urls import reverse
from django.test import TestCase
from model_mommy import mommy
from orcamentos.crm.models import Occupation


class OccupationTest(TestCase):

    def setUp(self):
        self.obj = Occupation.objects.create(occupation='Gerente')

    def test_create(self):
        self.assertTrue(Occupation.objects.exists())

    def test_str(self):
        self.assertEqual('Gerente', str(self.obj))


class OccupationTestCase(TestCase):

    def setUp(self):
        self.occupations = mommy.make('crm.Occupation', _quantity=10)

    def test_context(self):
        occupations = Occupation.objects.all()
        self.assertEquals(occupations.count(), 10)
