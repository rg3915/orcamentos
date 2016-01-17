# -*- coding: utf-8 -*-
import string
from random import random, randint, choice
from datetime import date, datetime, timedelta
from decimal import Decimal


def gen_string(max_length):
    return str(''.join(choice(string.ascii_letters) for i in range(max_length)))
gen_string.required = ['max_length']


def gen_age(min_age=15, max_age=99):
    # gera numeros inteiros entre 15 e 99
    return randint(min_age, max_age)


def gen_digits(max_length):
    return str(''.join(choice(string.digits) for i in range(max_length)))


def gen_doc(doc='cpf'):
    if doc == 'cpf':
        return gen_digits(11)
    elif doc == 'cnpj':
        return gen_digits(14)
    elif doc == 'rg':
        return gen_digits(10)


def gen_ncm():
    return gen_digits(8)


def gen_phone():
    # gera um telefone no formato (xx) xxxxx-xxxx
    digits_ = gen_digits(11)
    return '{} 9{}-{}'.format(digits_[:2], digits_[3:7], digits_[7:])


def gen_decimal(max_digits=5, decimal_places=2):
    num_as_str = lambda x: ''.join([str(randint(0, 9)) for i in range(x)])
    return Decimal("%s.%s" % (num_as_str(max_digits - decimal_places), num_as_str(decimal_places)))
gen_decimal.required = ['max_digits', 'decimal_places']


def gen_date(min_year=1915, max_year=1997):
    # gera um date no formato yyyy-mm-dd
    year = randint(min_year, max_year)
    month = randint(1, 12)
    day = randint(1, 28)
    d = date(year, month, day).isoformat()
    return d


def gen_timestamp(min_year=1915, max_year=1997):
    # gera um datetime no formato yyyy-mm-dd hh:mm:ss.000000
    min_date = datetime(min_year, 1, 1)
    max_date = datetime(max_year + 1, 1, 1)
    delta = random() * (max_date - min_date).total_seconds()
    return (min_date + timedelta(seconds=delta)).isoformat(" ")

''' sorteio que cai dia 29 de fevereiro
i,d=0,gen_timestamp()
while d[5:10] != '02-29' and i < 100000:
    i, d=i+1,gen_timestamp()

i,d
'''


def gen_ipi():
    num_as_str = lambda x: ''.join(
        [str(randint(0, 9)) for i in range(x)])
    return Decimal("0.%s" % (num_as_str(2)))


def gen_city():
    list_city = [
        [u'São Paulo', 'SP'],
        [u'Belém', 'PA'],
        [u'Rio de Janeiro', 'RJ'],
        [u'Goiânia', 'GO'],
        [u'Salvador', 'BA'],
        [u'Guarulhos', 'SP'],
        [u'Brasília', 'DF'],
        [u'Campinas', 'SP'],
        [u'Fortaleza', 'CE'],
        [u'São Luís', 'MA'],
        [u'Belo Horizonte', 'MG'],
        [u'São Gonçalo', 'RJ'],
        [u'Manaus', 'AM'],
        [u'Maceió', 'AL'],
        [u'Curitiba', 'PR'],
        [u'Duque de Caxias', 'RJ'],
        [u'Recife', 'PE'],
        [u'Natal', 'RN'],
        [u'Porto Alegre', 'RS'],
        [u'Campo Grande', 'MS']]
    return choice(list_city)


def gen_city_online():
    # https://raw.githubusercontent.com/felipefdl/cidades-estados-brasil-json/master/Cidades.json
    # fazer leitura de json, importar os dados e randomizar numa lista
    pass
