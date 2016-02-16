import io
import random
import names
import csv
from orcamentos.crm.models import Person, Occupation
from orcamentos.utils.lists import COMPANY_LIST
from orcamentos.utils.gen_random_values import *
from orcamentos.utils.gen_names import *

address_list = []
REPEAT = 48

''' Lendo os dados de enderecos_.csv '''
with open('fix/enderecos_.csv', 'r') as f:
    r = csv.DictReader(f)
    for dct in r:
        address_list.append(dct)
    f.close()

if not Occupation.objects.all().count():
    Occupation.objects.create(occupation=u'Arquiteto')
    Occupation.objects.create(occupation=u'Coordenador')
    Occupation.objects.create(occupation=u'Diretor')
    Occupation.objects.create(occupation=u'Engenheiro')
    Occupation.objects.create(occupation=u'Estagiário')
    Occupation.objects.create(occupation=u'Gerente')
    Occupation.objects.create(occupation=u'Orçamentista')
    Occupation.objects.create(occupation=u'Vendedor')


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

occupation = Occupation.objects.get(pk=4)
obj = Person(
    gender='M',
    treatment='sr',
    first_name='Adailton',
    last_name='do Nascimento',
    slug='adailton-do-nascimento',
    company='RG Solutions',
    department='Developer',
    occupation=occupation,
    email='dhelbegors@example.com',
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
    company = random.choice(COMPANY_LIST)
    cpf = gen_cpf()
    rg = gen_rg()
    obj = Person(
        gender=g,
        treatment=treatment,
        first_name=first_name,
        last_name=last_name,
        slug=first_name.lower() + '-' + last_name.lower(),
        company=company,
        occupation=occupation,
        email=first_name[0].lower() + '.' + last_name.lower() + '@example.com',
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
