import io
import random
import names
import csv
from django.db import IntegrityError
from orcamentos.crm.models import Person, Customer, Occupation
from orcamentos.proposal.models import Work
from orcamentos.utils.gen_random_values import *
from orcamentos.utils.gen_names import *
from orcamentos.utils.lists import CUSTOMER_TYPE, COMPANY_LIST, OCCUPATION_LIST

customer_list = []
work_list = []
address_list = []

''' Lendo os dados de obras_.csv '''
with open('fix/obras_.csv', 'r') as f:
    r = csv.DictReader(f)
    for dct in r:
        work_list.append(dct)
    f.close()

''' Lendo os dados de clientes_.csv '''
with open('fix/clientes_.csv', 'r') as f:
    r = csv.DictReader(f)
    for dct in r:
        customer_list.append(dct)
    f.close()

''' Lendo os dados de enderecos_.csv '''
with open('fix/enderecos_.csv', 'r') as f:
    r = csv.DictReader(f)
    for dct in r:
        address_list.append(dct)
    f.close()

if not Occupation.objects.all().count():
    obj = [Occupation(occupation=val) for val in OCCUPATION_LIST]
    Occupation.objects.bulk_create(obj)

if not Person.objects.all().count():
    occupation = Occupation.objects.get(pk=1)
    obj = Person(
        gender='M',
        treatment='sr',
        first_name='Regis',
        last_name='da Silva',
        slug='regis-da-silva',
        company='RG Solutions',
        department=u'Orçamentos',
        occupation=occupation,
        email='regis@example.com',
        cpf='11122233396',
        rg='40373800',
        address=u'Avenida Paulista, 1320',
        complement='Apto 303',
        district=u'Cerqueira César',
        city=u'São Paulo',
        uf='SP',
        cep='01020000',
        active=True,
    )
    obj.save()


if not Customer.objects.all().count():
    g = random.choice(['M', 'F'])
    if g == 'M':
        treatment = gen_male_first_name()['treatment']
        first_name = gen_male_first_name()['first_name']
    else:
        treatment = gen_female_first_name()['treatment']
        first_name = gen_female_first_name()['first_name']
    last_name = names.get_last_name()
    email = first_name[0].lower() + '.' + last_name.lower() + '@example.com'
    Customer.objects.create(
        gender='M',
        treatment='sr',
        first_name=first_name,
        last_name=last_name,
        slug=first_name.lower() + '-' + last_name.lower(),
        company=random.choice(COMPANY_LIST),
        email=email,
        customer_type=customer_list[0]['customer_type'],
        cpf=gen_cpf(),
        rg=gen_rg(),
        cnpj=gen_digits(14),
        ie='isento',
        address=address_list[0]['address'],
        district=address_list[0]['district'],
        city=address_list[0]['city'],
        uf=address_list[0]['uf'],
        cep=address_list[0]['cep'],
        active=True,
    )


REPEAT = len(work_list)

for i in range(REPEAT):
    p = 1  # randint(1, 50)
    person = Person.objects.get(pk=p)
    c = 1  # randint(1, 25)
    customer = Customer.objects.get(pk=c)
    obj = Work(
        name_work=work_list[i]['name_work'],
        slug=work_list[i]['slug'],
        person=person,
        customer=customer,
        address=address_list[i]['address'],
        district=address_list[i]['district'],
        city=address_list[i]['city'],
        uf=address_list[i]['uf'],
        cep=address_list[i]['cep'],
    )
    try:
        obj.save()
    except IntegrityError:
        print('Registro existente.')

# done
