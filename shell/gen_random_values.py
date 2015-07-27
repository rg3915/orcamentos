# -*- coding: utf-8 -*-
import random
import rstr
import datetime
from decimal import Decimal


def gen_age():
    return random.randint(18, 100)


def gen_doc(length=11):
    return rstr.rstr('1234567890', length)


def gen_phone():
    # gera um telefone no formato (xx) xxxx-xxxx
    return '{0} {1}-{2}'.format(
        rstr.rstr('1234567890', 2),
        rstr.rstr('1234567890', 4),
        rstr.rstr('1234567890', 4))


def gen_decimal(max_digits, decimal_places):
    num_as_str = lambda x: ''.join(
        [str(random.randint(0, 9)) for i in range(x)])
    return Decimal("%s.%s" % (num_as_str(max_digits - decimal_places),
                              num_as_str(decimal_places)))
gen_decimal.required = ['max_digits', 'decimal_places']


def gen_date(min_year=1915, max_year=1997):
    # gera um date no formato yyyy-mm-dd
    year = random.randint(min_year, max_year)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    date = datetime.date(year, month, day).isoformat()
    return date


def gen_timestamp(min_year=1915, max_year=1997):
    # gera um datetime no formato yyyy-mm-dd hh:mm:ss.000000
    year = random.randint(min_year, max_year)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    microsecond = random.randint(0, 999999)
    date = datetime.datetime(
        year, month, day, hour, minute, second, microsecond).isoformat(" ")
    return date


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
    return random.choice(list_city)
