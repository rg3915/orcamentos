# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy
from django.utils.formats import number_format
from django.contrib.auth.models import User
# List of values for use in choices
from .lists import gender_list, treatment_list, uf_list, \
    type_customer_list, priority_list, type_prop_list, status_list


class TimeStampedModel(models.Model):
    created = models.DateTimeField(
        _('criado em'), auto_now_add=True, auto_now=False)
    modified = models.DateTimeField(
        _('modificado em'), auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True


class Address(models.Model):
    address = models.CharField(_(u'endereço'), max_length=80)
    complement = models.CharField(

        _('complemento'), max_length=80, null=True, blank=True)
    district = models.CharField(
        _('bairro'), max_length=80, null=True, blank=True)
    city = models.CharField(_('cidade'), max_length=80)
    uf = models.CharField(_('UF'), max_length=2, choices=uf_list)
    cep = models.CharField(_('CEP'), max_length=9, null=True, blank=True)

    class Meta:
        abstract = True


class MyUser(models.Model):
    first_name = models.CharField(_('nome'), max_length=50)
    last_name = models.CharField(
        _('sobrenome'), max_length=50, null=True, blank=True)
    email = models.EmailField(_('e-mail'), null=True, blank=True)

    class Meta:
        abstract = True


class People(TimeStampedModel, Address):
    gender = models.CharField(_(u'gênero'), max_length=1, choices=gender_list)
    treatment = models.CharField(
        _('tratamento'), max_length=4, choices=treatment_list, null=True, blank=True)
    company = models.CharField(
        _('empresa'), max_length=50, null=True, blank=True)
    department = models.CharField(
        _('departamento'), max_length=50, null=True, blank=True)
    phone1 = models.CharField(
        _('fone 1'), max_length=20, null=True, blank=True)
    phone2 = models.CharField(
        _('fone 2'), max_length=20, null=True, blank=True)
    phone3 = models.CharField(
        _('fone 3'), max_length=20, null=True, blank=True)
    cpf = models.CharField(
        _('CPF'), max_length=11, unique=True, null=True, blank=True)
    rg = models.CharField(_('RG'), max_length=11, null=True, blank=True)
    active = models.BooleanField(_('ativo'), default=True)
    blocked = models.BooleanField(_('bloqueado'), default=False)

    class Meta:
        abstract = True

    def __str__(self):
        if self.last_name:
            return self.first_name + " " + self.last_name
        else:
            return self.first_name

    full_name = property(__str__)


class Person(MyUser, People):
    occupation = models.ForeignKey(
        "Occupation", verbose_name='cargo', related_name='person_occupation')

    class Meta:
        ordering = ['first_name']
        verbose_name = 'contato'
        verbose_name_plural = 'contatos'

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse_lazy('person_detail', kwargs={'pk': self.pk})


class Customer(MyUser, People):
    cnpj = models.CharField(
        _('CNPJ'), max_length=14, unique=True, null=True, blank=True)
    ie = models.CharField(
        _(u'inscrição estadual'), max_length=12, null=True, blank=True)
    type_customer = models.CharField(
        _('tipo de cliente'), max_length=1, choices=type_customer_list)

    class Meta:
        ordering = ['first_name']
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse_lazy('customer_detail', kwargs={'pk': self.pk})


class Employee(People):
    user = models.OneToOneField(User)
    occupation = models.ForeignKey(
        "Occupation", verbose_name='cargo', related_name='employee_occupation')
    date_entry = models.DateTimeField(
        _('data de entrada'), null=True, blank=True)
    date_release = models.DateTimeField(
        _(u'data de saída'), null=True, blank=True)

    class Meta:
        ordering = ['user__first_name']
        verbose_name = u'funcionário'
        verbose_name_plural = u'funcionários'

    def __str__(self):
        return str(self.user)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


class Occupation(models.Model):
    occupation = models.CharField(_('cargo'), max_length=50, unique=True)

    class Meta:
        ordering = ['occupation']
        verbose_name = _('cargo')
        verbose_name_plural = _('cargos')

    def __str__(self):
        return self.occupation


class Seller(models.Model):
    employee = models.OneToOneField(
        "Employee", verbose_name=u'funcionário', related_name='seller_employee')
    internal = models.BooleanField(_('interno'), default=True)
    commissioned = models.BooleanField(_('comissionado'), default=True)
    commission = models.DecimalField(
        _(u'comissão'), max_digits=6, decimal_places=2, default=0.01, blank=True)

    class Meta:
        ordering = ['employee__user__first_name']
        verbose_name = 'vendedor'
        verbose_name_plural = 'vendedores'

    def __str__(self):
        return str(self.employee)


class Entry(TimeStampedModel):
    priority = models.CharField(
        _('prioridade'), max_length=10, choices=priority_list, default='n')
    category = models.ForeignKey(
        "Category", verbose_name='categoria', related_name='entry_category')
    work = models.ForeignKey(
        "Work", verbose_name='obra', related_name='entry_work')
    person = models.ForeignKey(
        "Person", verbose_name='contato', related_name='entry_person')
    description = models.TextField(
        _(u'descrição'), max_length=100, null=True, blank=True)
    seller = models.ForeignKey(
        "Seller", verbose_name='vendedor', related_name='entry_seller')
    is_entry = models.BooleanField(_('dado entrada'), default=False)

    class Meta:
        ordering = ['created']
        verbose_name = 'entrada'
        verbose_name_plural = 'entradas'

    def __str__(self):
        return str(self.work)

    def get_absolute_url(self):
        return reverse_lazy('entry_detail', kwargs={'pk': self.pk})


class Category(models.Model):
    category = models.CharField(_('categoria'), max_length=20, unique=True)

    class Meta:
        ordering = ['category']
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.category


class Work(Address):
    name_work = models.CharField(_('obra'), max_length=100, unique=True)
    person = models.ForeignKey(
        "Person", verbose_name='contato', related_name='work_person')
    customer = models.ForeignKey(
        "Customer", verbose_name='cliente', related_name='work_customer')

    class Meta:
        ordering = ['name_work']
        verbose_name = 'obra'
        verbose_name_plural = 'obras'

    def __str__(self):
        return self.name_work

    def get_absolute_url(self):
        return reverse_lazy('work_detail', kwargs={'pk': self.pk})


class Proposal(TimeStampedModel):
    num_prop = models.PositiveIntegerField(_(u'número'))
    type_prop = models.CharField(
        _(u'tipo de orçamento'), max_length=20, choices=type_prop_list, null=True, blank=True)
    num_type_prop = models.PositiveIntegerField(
        _(u'número da revisão'), default=0)
    category = models.ForeignKey(
        "Category", verbose_name='categoria', related_name='proposal_category')
    description = models.CharField(
        _(u'descrição'), max_length=100, null=True, blank=True)
    work = models.ForeignKey(
        "Work", verbose_name='obra', related_name='proposal_work')
    person = models.ForeignKey(
        "Person", verbose_name='contato', related_name='proposal_person')
    employee = models.ForeignKey(
        "Employee", verbose_name=u'orçamentista', related_name='proposal_employee')
    seller = models.ForeignKey(
        "Seller", verbose_name='vendedor', related_name='proposal_seller')
    status = models.CharField(
        max_length=4, choices=status_list, default='elab')
    date_conclusion = models.DateTimeField(
        _(u'data de conclusão'), null=True, blank=True)
    price = models.DecimalField(
        _('valor'), max_digits=9, decimal_places=2, default=0)
    obs = models.TextField(
        _(u'observação'), max_length=100, null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = u'orçamento'
        verbose_name_plural = u'orçamentos'

    def __str__(self):
        # formato 001.15.0
        return u"%03d.%s.%d" % (self.num_prop, self.created.strftime('%y'), self.num_type_prop)
    codigo = property(__str__)

    def get_absolute_url(self):
        return reverse_lazy('proposal_detail', kwargs={'pk': self.pk})

    def get_price(self):
        return u"R$ %s" % number_format(self.price, 2)

    def get_customer(self):
        return self.work.customer
    cliente = property(get_customer)

    def get_customer_url(self):
        return u'/customer/%i' % self.work.customer.id

    def get_work_url(self):
        return u'/work/%i' % self.work.id

    def get_person_url(self):
        return u'/person/%i' % self.person.id

    def get_seller(self):
        return self.seller.employee.user.first_name

    def get_address(self):
        return u'%s, %s, %s - %s' % (self.work.address, self.work.district, self.work.city, self.work.uf)


class Contract(TimeStampedModel):
    proposal = models.OneToOneField(
        "Proposal", verbose_name=u'orçamento', related_name='contract_proposal')
    contractor = models.ForeignKey(
        "Customer", verbose_name=u'contratante', related_name='contract_customer')
    is_canceled = models.BooleanField(_('cancelado'), default=False)

    class Meta:
        ordering = ['proposal']
        verbose_name = u'contrato'
        verbose_name_plural = u'contratos'

    def __str__(self):
        return str(self.proposal)

    def get_absolute_url(self):
        return reverse_lazy('contract_detail', kwargs={'pk': self.pk})


class NumLastProposal(models.Model):
    num_last_prop = models.PositiveIntegerField(_(u'número'))

    class Meta:
        verbose_name = u'número último orçamento'
        verbose_name_plural = u'número último orçamento'

    def __str__(self):
        return str(self.num_last_prop)
