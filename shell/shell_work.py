import io
import random
import names
import csv
from core.models import Work, Person, Customer
from shell.gen_random_values import *

work_list = []
address_list = []

''' Lendo os dados de obras_.csv '''
with open('fixtures/obras_.csv', 'r') as f:
    r = csv.DictReader(f)
    for dct in r:
        work_list.append(dct)
    f.close()

''' Lendo os dados de enderecos_.csv '''
with open('fixtures/enderecos_.csv', 'r') as f:
    r = csv.DictReader(f)
    for dct in r:
        address_list.append(dct)
    f.close()

REPEAT = len(work_list)

for i in range(REPEAT):
    p = random.randint(1, 50)
    person = Person.objects.get(pk=p)
    c = random.randint(1, 25)
    customer = Customer.objects.get(pk=c)
    obj = Work(
        name_work=work_list[i]['name_work'],
        person=person,
        customer=customer,
        address=address_list[i]['address'],
        district=address_list[i]['district'],
        city=address_list[i]['city'],
        uf=address_list[i]['uf'],
        cep=address_list[i]['cep'],
    )
    obj.save()

print('%d Works salvo com sucesso.' % REPEAT)
