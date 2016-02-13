from django.db import models
from django.shortcuts import resolve_url as r
from orcamentos.core.models import TimeStampedModel, Address
from orcamentos.core.lists import PRIORITY, NORMAL, CATEGORY, PROP_TYPE, STATUS


class Entry(TimeStampedModel):
    priority = models.PositiveIntegerField(
        'prioridade', choices=PRIORITY, default=NORMAL)
    category = models.PositiveIntegerField(
        'categoria', choices=CATEGORY, default=1)
    work = models.ForeignKey(
        'Work', verbose_name='obra', related_name='entry_work')
    person = models.ForeignKey(
        'crm.Person', verbose_name='contato', related_name='entry_person')
    description = models.TextField('descrição', blank=True)
    seller = models.ForeignKey(
        'crm.Seller', verbose_name='vendedor', related_name='entry_seller', null=True, blank=True)
    is_entry = models.BooleanField('dado entrada', default=False)

    class Meta:
        ordering = ['priority', 'created']
        verbose_name = 'entrada'
        verbose_name_plural = 'entradas'

    def __str__(self):
        return str(self.work)

    def get_absolute_url(self):
        return r('proposal:entry_detail', pk=self.pk)


class Work(Address):
    name_work = models.CharField('obra', max_length=100, unique=True)
    slug = models.SlugField('slug')
    person = models.ForeignKey(
        'crm.Person', verbose_name='contato', related_name='work_person', null=True, blank=True)
    customer = models.ForeignKey(
        'crm.Customer', verbose_name='cliente', related_name='work_customer')

    class Meta:
        ordering = ['name_work']
        verbose_name = 'obra'
        verbose_name_plural = 'obras'

    def __str__(self):
        return self.name_work

    def get_absolute_url(self):
        return r('proposal:work_detail', slug=self.slug)


class Proposal(TimeStampedModel):
    num_prop = models.PositiveIntegerField(u'número')
    prop_type = models.CharField(
        u'tipo de orçamento', max_length=20, choices=PROP_TYPE, default='R')
    num_prop_type = models.PositiveIntegerField(
        u'número da revisão', default=0)
    category = models.PositiveIntegerField(
        'categoria', choices=CATEGORY, default=1)
    description = models.TextField(u'descrição', blank=True)
    work = models.ForeignKey(
        'Work', verbose_name='obra', related_name='proposal_work')
    person = models.ForeignKey(
        'crm.Person', verbose_name='contato', related_name='proposal_person', null=True, blank=True)
    employee = models.ForeignKey(
        'crm.Employee', verbose_name=u'orçamentista', related_name='proposal_employee')
    seller = models.ForeignKey(
        'crm.Seller', verbose_name='vendedor', related_name='proposal_seller', null=True, blank=True)
    status = models.CharField(
        max_length=4, choices=STATUS, default='elab')
    date_conclusion = models.DateTimeField(
        u'data de conclusão', null=True, blank=True)
    price = models.DecimalField(
        'valor', max_digits=9, decimal_places=2, default=0)
    obs = models.TextField(u'observação', blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = u'orçamento'
        verbose_name_plural = u'orçamentos'

    def __str__(self):
        # formato 001.15.0
        self.actual_year = self.created.strftime('%y')
        return "%03d.%s.%d" % (self.num_prop, self.actual_year, self.num_prop_type)
    codigo = property(__str__)

    def get_absolute_url(self):
        return r('proposal:proposal_detail', pk=self.pk)

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
        if self.seller:
            return self.seller.employee.user.first_name

    def get_address(self):
        if self.work.address:
            return '{}, {}, {} - {}'.format(self.work.address, self.work.district, self.work.city, self.work.uf)


class Contract(TimeStampedModel):
    proposal = models.OneToOneField(
        'Proposal', verbose_name=u'orçamento', related_name='contract_proposal')
    contractor = models.ForeignKey(
        'crm.Customer', verbose_name=u'contratante', related_name='contract_customer')
    is_canceled = models.BooleanField('cancelado', default=False)

    class Meta:
        ordering = ['proposal']
        verbose_name = u'contrato'
        verbose_name_plural = u'contratos'

    def __str__(self):
        return str(self.proposal)

    def get_absolute_url(self):
        return r('proposal:contract_detail', pk=self.pk)


class NumLastProposal(models.Model):
    num_last_prop = models.PositiveIntegerField(u'número')

    class Meta:
        verbose_name = u'número último orçamento'
        verbose_name_plural = u'número último orçamento'

    def __str__(self):
        return str(self.num_last_prop)
