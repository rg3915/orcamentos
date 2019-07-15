from django.urls import reverse
from django.test import TestCase
from model_mommy import mommy
from orcamentos.crm.models import Occupation


class OccupationTest(TestCase):

    def setUp(self):
        self.obj = Occupation.objects.create(occupation='Gerente')
        self.obj2 = Occupation.objects.create(occupation='Diretor')

    def test_create(self):
        self.assertTrue(Occupation.objects.exists())

    def test_str(self):
        self.assertEqual('Gerente', str(self.obj))

    def test_exists(self):
        occupations_list = ['Diretor', 'Gerente']
        occupations = Occupation.objects.filter(
            occupation__in=occupations_list).values_list('occupation', flat=True).order_by('occupation')
        self.assertSequenceEqual(occupations, occupations_list)


class OccupationTestCase(TestCase):

    def setUp(self):
        self.occupations = mommy.make('crm.Occupation', _quantity=10)

    def test_context(self):
        occupations = Occupation.objects.all()
        self.assertEquals(occupations.count(), 10)
