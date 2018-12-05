from django.db import models
from django.shortcuts import resolve_url as r
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from orcamentos.core.models import TimeStampedModel, Address
from .managers import CustomerManager, PersonManager, SellerManager
from orcamentos.utils.lists import GENDER, TREATMENT, PHONE_TYPE, PERSON_TYPE, CUSTOMER_TYPE


class People(TimeStampedModel, Address):
    gender = models.CharField(
        u'gênero',
        max_length=1,
        choices=GENDER,
        default='I',
        null=True,
        blank=True
    )
    treatment = models.CharField(
        'tratamento',
        max_length=4,
        choices=TREATMENT,
        null=True,
        blank=True
    )
    slug = models.SlugField('slug', blank=True)
    photo = models.URLField('foto', null=True, blank=True)
    birthday = models.DateTimeField('nascimento', null=True, blank=True)
    company = models.CharField('empresa', max_length=50, null=True, blank=True)
    department = models.CharField('departamento', max_length=50, blank=True)
    cpf = models.CharField(
        'CPF',
        max_length=11,
        unique=True,
        null=True,
        blank=True
    )
    rg = models.CharField(
        'RG',
        max_length=11,
        null=True,
        blank=True
    )
    cnpj = models.CharField(
        'CNPJ',
        max_length=14,
        unique=True,
        null=True,
        blank=True
    )
    ie = models.CharField(
        u'inscrição estadual',
        max_length=12,
        null=True,
        blank=True
    )
    active = models.BooleanField('ativo', default=True)
    blocked = models.BooleanField('bloqueado', default=False)

    class Meta:
        abstract = True

    def __str__(self):
        return ' '.join(filter(None, [self.get_treatment_display(), self.first_name, self.last_name]))

    full_name = property(__str__)


class Person(People):
    first_name = models.CharField('nome', max_length=50)
    last_name = models.CharField(
        'sobrenome',
        max_length=50,
        null=True,
        blank=True
    )
    email = models.EmailField(null=True, blank=True)
    occupation = models.ForeignKey(
        'Occupation',
        verbose_name='cargo',
        related_name='person_occupation',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    person_type = models.CharField(
        'cliente ou contato',
        max_length=1,
        choices=PERSON_TYPE,
        default='p'
    )
    customer_type = models.CharField(
        'tipo de cliente',
        max_length=1,
        choices=CUSTOMER_TYPE,
        blank=True
    )

    objects = PersonManager()

    class Meta:
        ordering = ['first_name']
        verbose_name = 'contato'
        verbose_name_plural = 'contatos'

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return r('crm:person_detail', slug=self.slug)

    def save(self):
        self.fullname = '{} {}'.format(self.first_name, self.last_name)
        self.slug = slugify(self.fullname)
        super(Person, self).save()


class PhonePerson(models.Model):
    phone = models.CharField('telefone', max_length=20, blank=True)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    phone_type = models.CharField(
        'tipo',
        max_length=3,
        choices=PHONE_TYPE,
        default='pri'
    )


class Customer(Person):
    objects = CustomerManager()

    class Meta:
        proxy = True
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'

    def get_absolute_url(self):
        return r('crm:customer_detail', slug=self.slug)


class Employee(People, User):
    occupation = models.ForeignKey(
        'Occupation',
        verbose_name='cargo',
        related_name='employee_occupation',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    internal = models.BooleanField('interno', default=True)
    commissioned = models.BooleanField('comissionado', default=True)
    commission = models.DecimalField(
        u'comissão',
        max_digits=6,
        decimal_places=2,
        default=0.01
    )
    date_release = models.DateTimeField(
        u'data de saída',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ['username']
        verbose_name = u'funcionário'
        verbose_name_plural = u'funcionários'


class PhoneEmployee(models.Model):
    phone = models.CharField('telefone', max_length=20, blank=True)
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    phone_type = models.CharField(
        'tipo',
        max_length=3,
        choices=PHONE_TYPE,
        default='pri'
    )


class Occupation(models.Model):
    occupation = models.CharField('cargo', max_length=50, unique=True)

    class Meta:
        ordering = ['occupation']
        verbose_name = 'cargo'
        verbose_name_plural = 'cargos'

    def __str__(self):
        return self.occupation


class Seller(Employee):
    objects = SellerManager()

    class Meta:
        proxy = True
        verbose_name = 'vendedor'
        verbose_name_plural = 'vendedores'
