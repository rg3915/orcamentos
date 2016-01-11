from django.contrib.auth.models import User
from orcamentos.core.models import Employee, Occupation

user = User.objects.get(username='amanda')
occupation = Occupation.objects.get(pk=3)
obj = Employee(
    user=user,
    occupation=occupation,
    date_entry='2015-12-03T01:47:17.524045Z',
    # date_release='',
    gender='F',
    treatment='aa',
    company='Tivit',
    department=u'Arquitetura',
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

user = User.objects.get(username='caio')
occupation = Occupation.objects.get(pk=4)
obj = Employee(
    user=user,
    occupation=occupation,
    date_entry='2015-01-02T15:25:35.127147Z',
    gender='M',
    treatment='eng',
    company='Tivit',
    department='Engenharia',
    phone1='(11) 7630-3598',
    phone2='(11) 0638-5029',
    phone3='(11) 1827-6927',
    cpf='73842008714',
    rg='506793799',
    address='Rua Marília de Dirceu, 1525',
    complement='Apto 16',
    district='Aclimação',
    city='São Paulo',
    uf='SP',
    cep='01100000',
    active=True,
)
obj.save()

user = User.objects.get(username='rebeca')
occupation = Occupation.objects.get(pk=6)
obj = Employee(
    user=user,
    occupation=occupation,
    date_entry='2015-11-14T09:41:02.105526Z',
    gender='F',
    treatment='',
    company='Titanium',
    department='Orçamentos',
    phone1='(11) 5941-2233',
    phone2='(11) 2887-3286',
    phone3='(11) 7757-6085',
    cpf='24644675769',
    rg='592288359',
    address='Rua Monte Belo, 704',
    complement='cj. 3',
    district='Vergueiro',
    city='São Paulo',
    uf='SP',
    cep='01289098',
    active=True,
)
obj.save()

user = User.objects.get(username='douglas')
occupation = Occupation.objects.get(pk=6)
obj = Employee(
    user=user,
    occupation=occupation,
    date_entry='2015-05-16T21:27:20.081572Z',
    gender='M',
    treatment='',
    company='Titanium',
    department='Suprimentos',
    phone1='(11) 0162-6907',
    phone2='(11) 9544-1853',
    # phone3='',
    cpf='96699840361',
    rg='224651880',
    address='Rua Dráusio Camargo, 440',
    # complement='',
        district='Paraíso',
        city='São Paulo',
        uf='SP',
        cep='02812750',
        active=True,
)
obj.save()

user = User.objects.get(username='jose')
occupation = Occupation.objects.get(pk=2)
obj = Employee(
    user=user,
    occupation=occupation,
    date_entry='2015-09-28T06:00:01.305367Z',
    gender='M',
    treatment='sr',
    company='Bot',
    department='Vendas',
    phone1='(11) 2821-6772',
    phone2='(11) 1784-3771',
    phone3='(11) 7896-0948',
    cpf='88922876699',
    rg='967728378',
    address='Estrada Macacu, 1530',
    # complement='',
        district='Centro',
        city='São Paulo',
        uf='SP',
        cep='01627400',
        active=True,
)
obj.save()

user = User.objects.get(username='alice')
occupation = Occupation.objects.get(pk=6)
obj = Employee(
    user=user,
    occupation=occupation,
    date_entry='2015-09-02T19:20:50.544045Z',
    gender='F',
    treatment='srta',
    company='Plan',
    department='Gerência',
    phone1='(11) 5872-4814',
    phone2='(11) 0911-8736',
    # phone3='',
    cpf='52168942960',
    rg='742367358',
    address='Rua Georgina Sá Leite Orcessi, 1851',
    # complement='',
        district='Santo Amaro',
        city='São Paulo',
        uf='SP',
        cep='02616720',
        active=True,
)
obj.save()

user = User.objects.get(username='carla')
occupation = Occupation.objects.get(pk=1)
obj = Employee(
    user=user,
    occupation=occupation,
    date_entry='2015-12-26T22:35:56.660885Z',
    gender='F',
    treatment='srta',
    company='Plan',
    department='Arquitetura',
    phone1='(11) 6297-4741',
    phone2='(11) 8955-2228',
    phone3='(11) 8369-8870',
    cpf='27663116303',
    rg='188830743',
    address='Rua Vinte e Oito, 1491',
    # complement='',
        district='Filipinas',
        city='São Paulo',
        uf='SP',
        cep='01327465',
        active=True,
)
obj.save()

user = User.objects.get(username='regis')
occupation = Occupation.objects.get(pk=5)
obj = Employee(
    user=user,
    occupation=occupation,
    date_entry='2015-06-07T00:32:48.285420Z',
    gender='M',
    treatment='',
    company='RG Solutions',
    department='TI',
    phone1='(11) 4470-4335',
    phone2='(11) 7137-0769',
    # phone3='',
    cpf='15895419181',
    rg='305467840',
    address='Praça Otaviano de Paulo, 89',
    complement='Apto 44',
    district='Pompéia',
    city='São Paulo',
    uf='SP',
    cep='01727389',
    active=True,
)
obj.save()

user = User.objects.get(username='adailton')
occupation = Occupation.objects.get(pk=6)
obj = Employee(
    user=user,
    occupation=occupation,
    date_entry='2015-06-07T00:32:48.285420Z',
    gender='M',
    treatment='',
    company='RG Solutions',
    department='TI',
    phone1='(11) 9002-9415',
    phone2='(11) 0444-0210',
    # phone3='',
    cpf='41895976210',
    rg='535121673',
    address='Rua Jaqueira, 460',
    # complement='',
        district='Santo Antonio',
        city='Aparecida de Goiânia',
        uf='GO',
        cep='10282900',
        active=True,
)
obj.save()
