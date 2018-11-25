import random
import names
import csv
from django.template.defaultfilters import slugify
from orcamentos.crm.models import Person, PhonePerson, Occupation
from orcamentos.utils.lists import COMPANY_LIST, OCCUPATION_LIST
from orcamentos.utils.gen_random_values import gen_phone, gen_rg, gen_cpf
from orcamentos.utils.gen_names import (
    gen_female_first_name,
    gen_male_first_name,
)

address_list = []
REPEAT = 48

''' Lendo os dados de enderecos_.csv '''
with open('fix/enderecos_.csv', 'r') as f:
    r = csv.DictReader(f)
    for dct in r:
        address_list.append(dct)
    f.close()

if not Occupation.objects.all().count():
    obj = [Occupation(occupation=val) for val in OCCUPATION_LIST]
    Occupation.objects.bulk_create(obj)


photo = 'http://icons.iconarchive.com/icons/icons-land/vista-people/256/Office-Customer-Male-Light-icon.png'

occupation = Occupation.objects.get(pk=1)
obj = Person(
    person_type='p',
    gender='M',
    treatment='sr',
    first_name='Regis',
    last_name='da Silva',
    slug='regis-da-silva',
    photo=photo,
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
    person_type='p',
    gender='M',
    treatment='sr',
    first_name='Adailton',
    last_name='do Nascimento',
    slug='adailton-do-nascimento',
    photo=photo,
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
    occupation_id = random.randint(1, 8)
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
    slug = slugify('{} {}'.format(first_name, last_name))
    obj = Person(
        person_type='p',
        gender=g,
        treatment=treatment,
        first_name=first_name,
        last_name=last_name,
        slug=slug,
        photo=photo,
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

'''
Para cada Person incluimos dois telefones:
um principal e um celular
'''
persons = Person.objects.all()
aux = []
for person in persons:
    obj_pri = PhonePerson(
        phone=gen_phone(),
        person=person,
    )
    obj = PhonePerson(
        phone=gen_phone(),
        person=person,
        phone_type='cel'
    )
    aux.append(obj_pri)
    aux.append(obj)
PhonePerson.objects.bulk_create(aux)
