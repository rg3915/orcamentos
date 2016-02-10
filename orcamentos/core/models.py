from django.db import models
from django.core.urlresolvers import reverse_lazy
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
    address = models.CharField(u'endereço', max_length=100)
    complement = models.CharField(
        'complemento', max_length=100, null=True, blank=True)
    district = models.CharField(
        'bairro', max_length=100, null=True, blank=True)
    city = models.CharField('cidade', max_length=100, null=True, blank=True)
    uf = models.CharField('UF', max_length=2, choices=UF_LIST)
    cep = models.CharField('CEP', max_length=9, null=True, blank=True)

    class Meta:
        abstract = True
