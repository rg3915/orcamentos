rm -rf temp
mkdir temp
echo "KeyStrPress Control_L KeyStrPress Shift_L KeyStrPress t KeyStrRelease t KeyStrRelease Control_L KeyStrRelease Shift_L" > temp/telas.txt

### sa.txt ###
cat << EOF > temp/sa.txt
String sa
KeyStrPress Return KeyStrRelease Return
EOF
### sa.txt ###

### shell.txt ###
cat << EOF > temp/shell.txt
String manage shell
KeyStrPress Return KeyStrRelease Return
EOF
### shell.txt ###

### file.txt ###
cat << EOF > temp/file.txt
String import io
KeyStrPress Return KeyStrRelease Return
String import random
KeyStrPress Return KeyStrRelease Return
String import names
KeyStrPress Return KeyStrRelease Return
String import csv
KeyStrPress Return KeyStrRelease Return
String from django.db import IntegrityError
KeyStrPress Return KeyStrRelease Return
String from orcamentos.crm.models import Person, Customer, Occupation
KeyStrPress Return KeyStrRelease Return
String from orcamentos.proposal.models import Work
KeyStrPress Return KeyStrRelease Return
String from orcamentos.utils.gen_random_values import *
KeyStrPress Return KeyStrRelease Return
String from orcamentos.utils.gen_names import *
KeyStrPress Return KeyStrRelease Return
String from orcamentos.utils.lists import CUSTOMER_TYPE, COMPANY_LIST, OCCUPATION_LIST
KeyStrPress Return KeyStrRelease Return

String customer_list = []
KeyStrPress Return KeyStrRelease Return
String work_list = []
KeyStrPress Return KeyStrRelease Return
String address_list = []
KeyStrPress Return KeyStrRelease Return
KeyStrPress Return KeyStrRelease Return
String with open('fix/obras_.csv', 'r') as f:
KeyStrPress Return KeyStrRelease Return
String     r = csv.DictReader(f)
KeyStrPress Return KeyStrRelease Return
String     for dct in r:
KeyStrPress Return KeyStrRelease Return
String         work_list.append(dct)
KeyStrPress Return KeyStrRelease Return
String     f.close()
KeyStrPress Return KeyStrRelease Return
KeyStrPress Return KeyStrRelease Return
String with open('fix/clientes_.csv', 'r') as f:
KeyStrPress Return KeyStrRelease Return
String     r = csv.DictReader(f)
KeyStrPress Return KeyStrRelease Return
String     for dct in r:
KeyStrPress Return KeyStrRelease Return
String         customer_list.append(dct)
KeyStrPress Return KeyStrRelease Return
String     f.close()
KeyStrPress Return KeyStrRelease Return
KeyStrPress Return KeyStrRelease Return
String with open('fix/enderecos_.csv', 'r') as f:
KeyStrPress Return KeyStrRelease Return
String     r = csv.DictReader(f)
KeyStrPress Return KeyStrRelease Return
String     for dct in r:
KeyStrPress Return KeyStrRelease Return
String         address_list.append(dct)
KeyStrPress Return KeyStrRelease Return
String     f.close()
KeyStrPress Return KeyStrRelease Return
KeyStrPress Return KeyStrRelease Return
String if not Occupation.objects.all().count():
KeyStrPress Return KeyStrRelease Return
String     obj = [Occupation(occupation=val) for val in OCCUPATION_LIST]
KeyStrPress Return KeyStrRelease Return
String     Occupation.objects.bulk_create(obj)
KeyStrPress Return KeyStrRelease Return
KeyStrPress Return KeyStrRelease Return

String if not Person.objects.all().count():
KeyStrPress Return KeyStrRelease Return
String     occupation = Occupation.objects.get(pk=1)
KeyStrPress Return KeyStrRelease Return
String     obj = Person(
    KeyStrPress Return KeyStrRelease Return
String         gender='M',
KeyStrPress Return KeyStrRelease Return
String         treatment='sr',
KeyStrPress Return KeyStrRelease Return
String         first_name='Regis',
KeyStrPress Return KeyStrRelease Return
String         last_name='da Silva',
KeyStrPress Return KeyStrRelease Return
String         slug='regis-da-silva',
KeyStrPress Return KeyStrRelease Return
String         company='RG Solutions',
KeyStrPress Return KeyStrRelease Return
String         department=u'Orcamentos',
KeyStrPress Return KeyStrRelease Return
String         occupation=occupation,
KeyStrPress Return KeyStrRelease Return
String         email='regis@example.com',
KeyStrPress Return KeyStrRelease Return
String         cpf='11122233396',
KeyStrPress Return KeyStrRelease Return
String         rg='40373800',
KeyStrPress Return KeyStrRelease Return
String         address=u'Avenida Paulista, 1320',
KeyStrPress Return KeyStrRelease Return
String         complement='Apto 303',
KeyStrPress Return KeyStrRelease Return
String         district=u'Cerqueira Cesar',
KeyStrPress Return KeyStrRelease Return
String         city=u'Sao Paulo',
KeyStrPress Return KeyStrRelease Return
String         uf='SP',
KeyStrPress Return KeyStrRelease Return
String         cep='01020000',
KeyStrPress Return KeyStrRelease Return
String         active=True,
KeyStrPress Return KeyStrRelease Return
String     )
KeyStrPress Return KeyStrRelease Return
String     obj.save()
KeyStrPress Return KeyStrRelease Return
KeyStrPress Return KeyStrRelease Return

String if not Customer.objects.all().count():
KeyStrPress Return KeyStrRelease Return
String     g = random.choice(['M', 'F'])
KeyStrPress Return KeyStrRelease Return
String     if g == 'M':
KeyStrPress Return KeyStrRelease Return
String         treatment = gen_male_first_name()['treatment']
KeyStrPress Return KeyStrRelease Return
String         first_name = gen_male_first_name()['first_name']
KeyStrPress Return KeyStrRelease Return
String     else:
KeyStrPress Return KeyStrRelease Return
String         treatment = gen_female_first_name()['treatment']
KeyStrPress Return KeyStrRelease Return
String         first_name = gen_female_first_name()['first_name']
KeyStrPress Return KeyStrRelease Return
String     last_name = names.get_last_name()
KeyStrPress Return KeyStrRelease Return
String     email = first_name[0].lower() + '.' + last_name.lower() + '@example.com'
KeyStrPress Return KeyStrRelease Return
String     Customer.objects.create(
KeyStrPress Return KeyStrRelease Return
String         gender='M',
KeyStrPress Return KeyStrRelease Return
String         treatment='sr',
KeyStrPress Return KeyStrRelease Return
String         first_name=first_name,
KeyStrPress Return KeyStrRelease Return
String         last_name=last_name,
KeyStrPress Return KeyStrRelease Return
String         slug=first_name.lower() + '-' + last_name.lower(),
KeyStrPress Return KeyStrRelease Return
String         company=random.choice(COMPANY_LIST),
KeyStrPress Return KeyStrRelease Return
String         email=email,
KeyStrPress Return KeyStrRelease Return
String         customer_type=customer_list[0]['customer_type'],
KeyStrPress Return KeyStrRelease Return
String         cpf=gen_cpf(),
KeyStrPress Return KeyStrRelease Return
String         rg=gen_rg(),
KeyStrPress Return KeyStrRelease Return
String         cnpj=gen_digits(14),
KeyStrPress Return KeyStrRelease Return
String         ie='isento',
KeyStrPress Return KeyStrRelease Return
String         address=address_list[0]['address'],
KeyStrPress Return KeyStrRelease Return
String         district=address_list[0]['district'],
KeyStrPress Return KeyStrRelease Return
String         city=address_list[0]['city'],
KeyStrPress Return KeyStrRelease Return
String         uf=address_list[0]['uf'],
KeyStrPress Return KeyStrRelease Return
String         cep=address_list[0]['cep'],
KeyStrPress Return KeyStrRelease Return
String         active=True,
KeyStrPress Return KeyStrRelease Return
String     )
KeyStrPress Return KeyStrRelease Return
KeyStrPress Return KeyStrRelease Return

String REPEAT = len(work_list)
KeyStrPress Return KeyStrRelease Return
KeyStrPress Return KeyStrRelease Return

String for i in range(REPEAT):
KeyStrPress Return KeyStrRelease Return
KeyStrPress Return KeyStrRelease Return
String     p = randint(1, 50)
KeyStrPress Return KeyStrRelease Return
String     person = Person.objects.get(pk=1)
KeyStrPress Return KeyStrRelease Return
String     c = randint(1, 25)
KeyStrPress Return KeyStrRelease Return
String     customer = Customer.objects.get(pk=1)
KeyStrPress Return KeyStrRelease Return
String     obj = Work(
KeyStrPress Return KeyStrRelease Return
String         name_work=work_list[i]['name_work'],
KeyStrPress Return KeyStrRelease Return
String         slug=work_list[i]['slug'],
KeyStrPress Return KeyStrRelease Return
String         person=person,
KeyStrPress Return KeyStrRelease Return
String         customer=customer,
KeyStrPress Return KeyStrRelease Return
String         address=address_list[i]['address'],
KeyStrPress Return KeyStrRelease Return
String         district=address_list[i]['district'],
KeyStrPress Return KeyStrRelease Return
String         city=address_list[i]['city'],
KeyStrPress Return KeyStrRelease Return
String         uf=address_list[i]['uf'],
KeyStrPress Return KeyStrRelease Return
String         cep=address_list[i]['cep'],
KeyStrPress Return KeyStrRelease Return
String     )
KeyStrPress Return KeyStrRelease Return
String     try:
KeyStrPress Return KeyStrRelease Return
String         obj.save()
KeyStrPress Return KeyStrRelease Return
String     except IntegrityError:
KeyStrPress Return KeyStrRelease Return
String         print('Registro existente.')
KeyStrPress Return KeyStrRelease Return
KeyStrPress Return KeyStrRelease Return
KeyStrPress Return KeyStrRelease Return
String # done
KeyStrPress Return KeyStrRelease Return

EOF
### file.txt ###

# xmacroplay
xmacroplay -d 10 < temp/telas.txt
sleep 1
xmacroplay -d 10 < temp/sa.txt
sleep 2
xmacroplay -d 10 < temp/shell.txt
sleep 3
xmacroplay -d 10 < temp/file.txt
