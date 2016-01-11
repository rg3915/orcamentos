import io
import random
import names
import csv
from orcamentos.core.models import Customer
from shell.gen_random_values import *
from shell.gen_names import *

type_customer = (
    ('c', 'construtora'),
    ('a', 'arquitetura'),
    ('p', 'particular')
)


company_list = (
    ('Acme'),
    ('Cyberdyne'),
    ('Globex'),
    ('Gringotes'),
    ('ILM'),
    ('Oscorp'),
    ('Tivit'),
    ('Wayne'),
)

customer_list = []
address_list = []

''' Lendo os dados de clientes_.csv '''
with open('fixtures/clientes_.csv', 'r') as f:
    r = csv.DictReader(f)
    for dct in r:
        customer_list.append(dct)
    f.close()

''' Lendo os dados de enderecos_.csv '''
with open('fixtures/enderecos_.csv', 'r') as f:
    r = csv.DictReader(f)
    for dct in r:
        address_list.append(dct)
    f.close()

REPEAT = len(customer_list) + 8

for i in range(REPEAT):
    g = random.choice(['M', 'F'])
    if g == 'M':
        treatment = gen_male_first_name()['treatment']
        first_name = gen_male_first_name()['first_name']
    else:
        treatment = gen_female_first_name()['treatment']
        first_name = gen_female_first_name()['first_name']
    last_name = names.get_last_name()
    phone1 = gen_phone()
    phone2 = gen_phone()
    phone3 = gen_phone()
    if i < 17:
        gender = 'M'
        treatment = None
        first_name = customer_list[i]['first_name']
        last_name = None
        company = None
        type_customer = customer_list[i]['type_customer']
        email = None
    else:
        gender = g
        company = random.choice(company_list)
        # department=''
        type_customer = 'p'
        email = first_name[0].lower() + \
            '.' + last_name.lower() + '@example.com'
    if type_customer == 'p':
        cpf = gen_doc()
        rg = gen_doc(9)
        cnpj = None
        ie = None
    else:
        cpf = None
        rg = None
        cnpj = gen_doc(14)
        ie = 'isento'
    Customer.objects.create(
        gender=g,
        treatment=treatment,
        first_name=first_name,
        last_name=last_name,
        company=company,
        # department='',
        email=email,
        phone1=phone1,
        phone2=phone2,
        phone3=phone3,
        type_customer=type_customer,
        cpf=cpf,
        rg=rg,
        cnpj=cnpj,
        ie=ie,
        address=address_list[i]['address'],
        district=address_list[i]['district'],
        city=address_list[i]['city'],
        uf=address_list[i]['uf'],
        cep=address_list[i]['cep'],
        active=True,
    )

print('%d Customers salvo com sucesso.' % REPEAT)
