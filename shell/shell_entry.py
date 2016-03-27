import random
import names
import csv
from django.db import IntegrityError
from django.template.defaultfilters import slugify
from orcamentos.utils.gen_random_values import gen_string
from orcamentos.crm.models import Employee, Customer, Person, Seller, Occupation
from orcamentos.proposal.models import Entry, Work
from orcamentos.utils.gen_random_values import *
from orcamentos.utils.gen_names import *
from orcamentos.utils.lists import URGENTE, ALTA, NORMAL, BAIXA, OCCUPATION_LIST, COMPANY_LIST


# ------------ Employee -------------------------
hashpass = 'pbkdf2_sha256$12000$Pe4addAsDo1D$xEtHWLnSIVkEppr4pbK69SBhuLwWsSHdXyhkCZBNktA='

# Primeiro verifica se existe os cargos, caso contrário os grava.
if not Occupation.objects.all().count():
    obj = [Occupation(occupation=val) for val in OCCUPATION_LIST]
    Occupation.objects.bulk_create(obj)


def get_occupation(occupation_name):
    occupation = Occupation.objects.get(occupation=occupation_name)
    return occupation


employees = {
    'jose': {
        'username': 'jose',
        'first_name': 'José',
        'last_name': 'Carlos Frederico',
        'occupation': 'Vendedor',
        'gender': 'M',
        'treatment': 'sr',
        'company': 'Bot',
        'department': 'Vendas',
        'cpf': '88922876699',
        'rg': '967728378',
        'address': 'Estrada Macacu, 1530',
        'complement': '',
        'district': 'Centro',
        'city': 'São Paulo',
        'uf': 'SP',
        'cep': '01627400'},
    'regis': {
        'username': 'regis',
        'first_name': 'Regis',
        'last_name': 'da Silva Santos',
        'occupation': 'Vendedor',
        'gender': 'M',
        'treatment': '',
        'company': 'RG Solutions',
        'department': 'TI',
        'cpf': '15895419181',
        'rg': '305467840',
        'address': 'Praça Otaviano de Paulo, 89',
        'complement': 'Apto 44',
        'district': 'Pompéia',
        'city': 'São Paulo',
        'uf': 'SP',
        'cep': '01727389'},
    'adailton': {
        'username': 'adailton',
        'first_name': 'Adailton',
        'last_name': 'do Nascimento',
        'occupation': 'Vendedor',
        'gender': 'M',
        'treatment': '',
        'company': 'RG Solutions',
        'department': 'TI',
        'cpf': '41895976210',
        'rg': '535121673',
        'address': 'Rua Jaqueira, 460',
        'complement': '',
        'district': 'Santo Antonio',
        'city': 'Aparecida de Goiânia',
        'uf': 'GO',
        'cep': '10282900'}
}


for k in employees:
    slug = slugify('{} {}'.format(
        employees[k]['first_name'], employees[k]['last_name']))
    Employee.objects.create(
        username=employees[k]['username'],
        first_name=employees[k]['first_name'],
        last_name=employees[k]['last_name'],
        slug=slug,
        email=employees[k]['username'] + '@example.com',
        is_staff=True,
        password=hashpass,
        occupation=get_occupation(employees[k]['occupation']),
        gender=employees[k]['gender'],
        treatment=employees[k]['treatment'],
        company=employees[k]['company'],
        department=employees[k]['department'],
        cpf=employees[k]['cpf'],
        rg=employees[k]['rg'],
        address=employees[k]['address'],
        complement=employees[k]['complement'],
        district=employees[k]['district'],
        city=employees[k]['city'],
        uf=employees[k]['uf'],
        cep=employees[k]['cep'],
    )

# ------------ Work -------------------------
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

photo = 'http://icons.iconarchive.com/icons/icons-land/vista-people/256/Office-Customer-Male-Light-icon.png'

if not Person.objects.all().count():
    for i in range(25):
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
        email = first_name[0].lower() + '.' + \
            last_name.lower() + '@example.com'
        obj = Person(
            person_type='p',
            gender='M',
            treatment=treatment,
            first_name=first_name,
            last_name=last_name,
            slug=slug,
            photo=photo,
            company=company,
            occupation=occupation,
            email=email,
            cpf=gen_cpf(),
            rg=gen_rg(),
            address=address_list[i]['address'],
            district=address_list[i]['district'],
            city=address_list[i]['city'],
            uf=address_list[i]['uf'],
            cep=address_list[i]['cep'],
        )
        obj.save()


if not Customer.objects.all().count():
    for i in range(len(customer_list)):
        g = random.choice(['M', 'F'])
        if g == 'M':
            treatment = gen_male_first_name()['treatment']
            first_name = gen_male_first_name()['first_name']
        else:
            treatment = gen_female_first_name()['treatment']
            first_name = gen_female_first_name()['first_name']
        last_name = names.get_last_name()
        email = first_name[0].lower() + '.' + \
            last_name.lower() + '@example.com'
        slug = slugify('{} {}'.format(first_name, last_name))
        obj = Customer(
            person_type='c',
            gender='M',
            treatment='sr',
            first_name=first_name,
            last_name=last_name,
            slug=slug,
            company=random.choice(COMPANY_LIST),
            email=email,
            customer_type=customer_list[0]['customer_type'],
            cpf=gen_cpf(),
            rg=gen_rg(),
            cnpj=gen_digits(14),
            ie='isento',
            address=address_list[i]['address'],
            district=address_list[i]['district'],
            city=address_list[i]['city'],
            uf=address_list[i]['uf'],
            cep=address_list[i]['cep'],
        )
        obj.save()


REPEAT = len(work_list)

for i in range(REPEAT):
    # obtem todos os pk de contatos
    person_pks = [pk[0] for pk in Person.objects.all().values_list('pk')]
    p = choice(person_pks)
    person = Person.objects.get(pk=p)
    # obtem todos os pk de clientes
    customer_pks = [pk[0] for pk in Customer.objects.all().values_list('pk')]
    c = choice(customer_pks)
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


# ------------ Entry -------------------------
priority_list = (URGENTE, ALTA, NORMAL, BAIXA)


# Return min id of work
try:
    min_work_pk = Work.objects.order_by('pk')[0].pk
except IndexError:
    min_work_pk = None


# Return max id of work
try:
    max_work_pk = Work.objects.latest('pk').id
except Work.DoesNotExist:
    max_work_pk = None


REPEAT = max_work_pk + 1

for i in range(min_work_pk, REPEAT):
    priority = choice(priority_list)
    work = Work.objects.get(pk=i)
    # obtem todos os pk de contatos
    person_pks = [pk[0] for pk in Person.objects.all().values_list('pk')]
    p = choice(person_pks)
    person = Person.objects.get(pk=p)
    # obtem todos os pk de vendedores
    seller_pks = [pk[0] for pk in Seller.objects.all().values_list('pk')]
    c = choice(seller_pks)
    seller = Seller.objects.get(pk=c)
    description = gen_string(30)
    obj = Entry(
        priority=priority,
        work=work,
        person=person,
        description=description,
        seller=seller,
    )
    obj.save()


# done
