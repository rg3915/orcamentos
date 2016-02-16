from django.db import models
from django.dispatch import receiver
from django.db.models import signals
from django.shortcuts import resolve_url as r
from django.contrib.auth.models import User
from orcamentos.core.models import TimeStampedModel, Address
from orcamentos.utils.lists import GENDER, TREATMENT, PHONE_TYPE, CUSTOMER_TYPE
from orcamentos.crm.validate.validate_documents import cnpj


class People(TimeStampedModel, Address):
    gender = models.CharField(u'gênero', max_length=1,
                              choices=GENDER, null=True, blank=True)
    treatment = models.CharField(
        'tratamento', max_length=4, choices=TREATMENT, null=True, blank=True)
    slug = models.SlugField('slug')
    photo = models.URLField('foto', null=True, blank=True)
    birthday = models.DateTimeField('nascimento', null=True, blank=True)
    company = models.CharField('empresa', max_length=50, null=True, blank=True)
    department = models.CharField(
        'departamento', max_length=50, null=True, blank=True)
    cpf = models.CharField(
        'CPF', max_length=11, unique=True, null=True, blank=True)
    rg = models.CharField('RG', max_length=11, null=True, blank=True)
    active = models.BooleanField('ativo', default=True)
    blocked = models.BooleanField('bloqueado', default=False)

    class Meta:
        abstract = True

    def __str__(self):
        return ' '.join(filter(None, [self.get_treatment_display(), self.first_name, self.last_name]))

    full_name = property(__str__)


class Phone(models.Model):
    phone = models.CharField('telefone', max_length=20, blank=True)
    person = models.ForeignKey('Person')
    phone_type = models.CharField(
        'tipo', max_length=3, choices=PHONE_TYPE, default='pri')


class Person(People):
    first_name = models.CharField('nome', max_length=50)
    last_name = models.CharField('sobrenome', max_length=50, blank=True)
    email = models.EmailField(null=True, blank=True)
    occupation = models.ForeignKey(
        'Occupation', verbose_name='cargo', related_name='person_occupation', null=True, blank=True)

    class Meta:
        ordering = ['first_name']
        verbose_name = 'contato'
        verbose_name_plural = 'contatos'

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return r('crm:person_detail', slug=self.slug)


class Customer(People):
    first_name = models.CharField('nome', max_length=50)
    last_name = models.CharField('sobrenome', max_length=50, blank=True)
    email = models.EmailField(null=True, blank=True)
    cnpj = models.CharField('CNPJ', max_length=14,
                            unique=True, null=True, blank=True, validators=[cnpj])
    ie = models.CharField(u'inscrição estadual', max_length=12, blank=True)
    customer_type = models.CharField(
        'tipo', max_length=1, choices=CUSTOMER_TYPE)

    class Meta:
        ordering = ['first_name']
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return r('crm:customer_detail', slug=self.slug)


class Employee(People):
    user = models.OneToOneField(User)
    occupation = models.ForeignKey(
        'Occupation', verbose_name='cargo', related_name='employee_occupation', null=True, blank=True)
    date_entry = models.DateTimeField('data de entrada', null=True, blank=True)
    date_release = models.DateTimeField(
        u'data de saída', null=True, blank=True)

    class Meta:
        ordering = ['user__first_name']
        verbose_name = u'funcionário'
        verbose_name_plural = u'funcionários'

    def __str__(self):
        return str(self.user)


# @receiver(signals.post_save, sender=User)
# def create_employee(sender, instance, created, **kwargs):
#     # Create employee
#     if created:
#         Employee.objects.get_or_create(
#             user=instance, slug=str(instance), date_entry=instance.date_joined)
#         print('Instance: ' + str(instance))


class Occupation(models.Model):
    occupation = models.CharField('cargo', max_length=50, unique=True)

    class Meta:
        ordering = ['occupation']
        verbose_name = 'cargo'
        verbose_name_plural = 'cargos'

    def __str__(self):
        return self.occupation


class Seller(models.Model):
    employee = models.OneToOneField(
        'Employee', verbose_name=u'funcionário', related_name='seller_employee')
    internal = models.BooleanField('interno', default=True)
    commissioned = models.BooleanField('comissionado', default=True)
    commission = models.DecimalField(
        u'comissão', max_digits=6, decimal_places=2, default=0.01)

    class Meta:
        ordering = ['employee__user__first_name']
        verbose_name = 'vendedor'
        verbose_name_plural = 'vendedores'

    def __str__(self):
        return str(self.employee)
