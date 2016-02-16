import io
import random
import names
import csv
from orcamentos.crm.models import Customer
from orcamentos.utils.lists import CUSTOMER_TYPE, COMPANY_LIST
from orcamentos.utils.gen_random_values import *
from orcamentos.utils.gen_names import *


customer_list = []
address_list = []

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
    if i < 17:
        gender = 'M'
        treatment = None
        first_name = customer_list[i]['first_name']
        last_name = None
        company = None
        customer_type = customer_list[i]['customer_type']
        email = None
    else:
        gender = g
        company = random.choice(COMPANY_LIST)
        # department=''
        customer_type = 'p'
        email = first_name[0].lower() + '.' + \
            last_name.lower() + '@example.com'
    if customer_type == 'p':
        cpf = gen_cpf()
        rg = gen_rg()
        cnpj = None
        ie = None
    else:
        cpf = None
        rg = None
        cnpj = gen_digits(14)
        ie = 'isento'
    Customer.objects.create(
        gender=g,
        treatment=treatment,
        first_name=first_name,
        last_name=last_name,
        company=company,
        # department='',
        email=email,
        customer_type=customer_type,
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

# print('%d Customers salvo com sucesso.' % REPEAT)
# done
