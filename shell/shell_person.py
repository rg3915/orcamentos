import io
import random
import names
import csv
from core.models import Person, Occupation
from shell.gen_random_values import *
from shell.gen_names import *

company_list = (
    ('Acme'),
    ('Cyberdyne'),
    ('Ghostbusters'),
    ('Globex'),
    ('Gringotes'),
    ('ILM'),
    ('Oscorp'),
    ('RG Solutions'),
    ('Stark'),
    ('Tabajara'),
    ('Teknotronic'),
    ('Tivit'),
    ('Wayne'),
    ('Wonka'),
)

address_list = []
REPEAT = 48

''' Lendo os dados de enderecos_.csv '''
with open('fixtures/enderecos_.csv', 'r') as f:
    r = csv.DictReader(f)
    for dct in r:
        address_list.append(dct)
    f.close()

occupation = Occupation.objects.get(pk=1)
obj = Person(
    gender='M',
    treatment='sr',
    first_name='Regis',
    last_name='da Silva',
    company='RG Solutions',
    department=u'Orçamentos',
    occupation=occupation,
    email='regis@example.com',
    phone1='11 7543-2101',
    phone2='11 7543-2102',
    phone3='11 7543-2103',
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

occupation = Occupation.objects.get(pk=4)
obj = Person(
    gender='M',
    treatment='sr',
    first_name='Adailton',
    last_name='do Nascimento',
    company='RG Solutions',
    department='Developer',
    occupation=occupation,
    email='dhelbegors@example.com',
    phone1='50 7543-2101',
    phone2='50 7543-2102',
    phone3='50 7543-2103',
    cpf='45877531140',
    rg='50373801',
    address=u'Rua Rafael Barbosa',
    complement='casa 1',
    district=u'Ribeirinho',
    city=u'Goiás',
    uf='GO',
    cep='01020000',
    active=True,
)

obj.save()

for i in range(REPEAT):
    occupation_id = random.randint(1, 1)
    occupation = Occupation.objects.get(pk=occupation_id)
    g = random.choice(['M', 'F'])
    if g == 'M':
        treatment = gen_male_first_name()['treatment']
        first_name = gen_male_first_name()['first_name']
    else:
        treatment = gen_female_first_name()['treatment']
        first_name = gen_female_first_name()['first_name']
    last_name = names.get_last_name()
    company = random.choice(company_list)
    phone1 = gen_phone()
    phone2 = gen_phone()
    phone3 = gen_phone()
    cpf = gen_doc()
    rg = gen_doc(9)
    obj = Person(
        gender=g,
        treatment=treatment,
        first_name=first_name,
        last_name=last_name,
        company=company,
        occupation=occupation,
        email=first_name[0].lower() + '.' + last_name.lower() + '@example.com',
        phone1=phone1,
        phone2=phone2,
        phone3=phone3,
        cpf=cpf,
        rg=rg,
        address=address_list[i]['address'],
        district=address_list[i]['district'],
        city=address_list[i]['city'],
        uf=address_list[i]['uf'],
        cep=address_list[i]['cep'],
        active=True,
    )
    obj.save()

print('%d Persons salvo com sucesso.' % REPEAT)
