import string
import requests
from random import random, randint, choice, randrange
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


def gen_rg():
    return gen_digits(10)


def gen_cpf():
    def calcula_digito(digs):
        s = 0
        qtd = len(digs)
        for i in range(qtd):
            s += n[i] * (1 + qtd - i)
        res = 11 - s % 11
        if res >= 10:
            return 0
        return res
    n = [randrange(10) for i in range(9)]
    n.append(calcula_digito(n))
    n.append(calcula_digito(n))
    return "%d%d%d%d%d%d%d%d%d%d%d" % tuple(n)


def gen_ncm():
    return gen_digits(8)


def gen_phone():
    # gera um telefone no formato xx xxxxx-xxxx
    digits_ = gen_digits(11)
    return '{} 9{}-{}'.format(digits_[:2], digits_[3:7], digits_[7:])


def gen_decimal(max_digits=5, decimal_places=2):
    num_as_str = lambda x: ''.join([str(randint(0, 9)) for i in range(x)])
    return Decimal("%s.%s" % (num_as_str(max_digits - decimal_places), num_as_str(decimal_places)))
gen_decimal.required = ['max_digits', 'decimal_places']


def gen_date(min_year=1900, max_year=datetime.now().year):
    # gera um date no formato yyyy-mm-dd
    start = date(min_year, 1, 1)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    return start + (end - start) * random.random()


def gen_datetime(min_year=1900, max_year=datetime.now().year):
    # gera um datetime no formato yyyy-mm-dd hh:mm:ss.000000
    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    return start + (end - start) * random.random()


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


def connect(url):
    return requests.get(url)


def gen_city():
    # json da Cidade
    jc = connect(url_city).json()
    # Escolhe uma Cidade aleatoriamente
    return jc[randint(0, 5563)]


def gen_state():
    # json do Estado
    js = connect(url_state).json()
    # Escolhe um Estado aleatoriamente
    return js[randint(0, 26)]


def city_and_state():
    # json da Cidade
    jc = connect(url_city).json()
    # Escolhe uma Cidade aleatoriamente
    city = jc[randint(0, 5563)]
    # Retorna o ID do Estado da respectiva Cidade
    state = int(city['Estado'])
    # json do Estado
    js = connect(url_state).json()
    # Escolhe o Estado pelo ID da respectiva Cidade
    state = js[state - 1]
    context = []
    context.append(city)
    context.append(state)
    return context
