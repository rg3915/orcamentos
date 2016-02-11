from django.db import models
# List of values for use in choices
from .lists import UF_LIST


class TimeStampedModel(models.Model):
    created = models.DateTimeField(
        'criado em', auto_now_add=True, auto_now=False)
    modified = models.DateTimeField(
        'modificado em', auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True


class Address(models.Model):
    address = models.CharField(u'endereço', max_length=100, blank=True)
    complement = models.CharField('complemento', max_length=100, blank=True)
    district = models.CharField('bairro', max_length=100, blank=True)
    city = models.CharField('cidade', max_length=100, blank=True)
    uf = models.CharField('UF', max_length=2, choices=UF_LIST)
    cep = models.CharField('CEP', max_length=9, blank=True)

    class Meta:
        abstract = True
