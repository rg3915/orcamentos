from django.test import TestCase
from datetime import datetime
from orcamentos.core.models import TimeStampedModel, Address


class AddressModelTest(TestCase):

    def setUp(self):
        self.obj = Address(
            address=u'Avenida Paulista, 1605',
            complement='Apto 303',
            district=u'Bela Vista',
            city=u'São Paulo',
            uf='SP',
            cep='01311200')
        self.obj.save()
