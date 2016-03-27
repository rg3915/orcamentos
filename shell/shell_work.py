import random
import names
import csv
from django.db import IntegrityError
from django.template.defaultfilters import slugify
from orcamentos.crm.models import Person, Customer, Occupation
from orcamentos.proposal.models import Work
from orcamentos.utils.gen_random_values import *
from orcamentos.utils.gen_names import *
from orcamentos.utils.lists import COMPANY_LIST, OCCUPATION_LIST

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


# done
