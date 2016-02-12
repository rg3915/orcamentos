import string
import requests
import names
from random import random, randint, choice, randrange
from datetime import date, datetime, timedelta
from decimal import Decimal

# INCOMPLETE...


class Provider(AddressProvider):
    street_prefixes = ('Alameda', 'Avenida', 'Estrada',
                       'Largo', 'Praça', 'Rua', 'Travessa')

    street_name_formats = (
        '{{street_prefix}} {{first_name}} {{last_name}}',
    )

    bairros = ('Acaiaca', 'Aguas Claras', 'Alpes', 'Alto Barroca', 'Alto Dos Pinheiros',
               'Alto Vera Cruz', 'Anchieta', 'Bacurau', 'Bandeirantes', 'Barreiro',
               'Barroca', 'Belmonte', 'Bonfim', 'Bonsucesso', 'Cachoeirinha', 'Caiçaras',
               'Califórnia', 'Diamante', 'Dom Joaquim', 'Embaúbas', 'Esplanada', 'Estrela',
               'Floramar', 'Floresta', 'Garças', 'Glória', 'Grajaú', 'Horto Florestal',
               'Indaiá', 'Ipe', 'Ipiranga', 'Itaipu''Jaraguá', 'Jardim Alvorada',
               'Jardinópolis', 'Jatobá', 'Lagoa', 'Laranjeiras', 'Liberdade',
               'Madri', 'Manacas', 'Miramar', 'Nova America', 'Novo Tupi', 'Oeste',
               'Pantanal', 'Renascença', 'Santa Inês', 'Santa Sofia', 'Teixeira Dias',
               'Tiradentes', 'Urca', 'Vera Cruz', 'Vila Da Luz', 'Vila Pilar',
               'Vitoria', 'Xangri-Lá', 'Zilah Sposito', )

    estados = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'))

    address_formats = (
        "{{street_name_formats}}, {{gen_number}}",
    )

    def address(self):
        """
        :example 'Rua Eurides da Cunha, 116'
        """
        pattern = self.random_element(self.address_formats)
        return self.generator.parse(pattern)

    @classmethod
    def street_prefix(cls):
        """
        :example 'rua'
        """
        return cls.random_element(cls.street_prefixes)

    @classmethod
    def estado(cls):
        """
        Randomly returns a Brazilian State  ('sigla' , 'nome').
        :example ('MG' . 'Minas Gerais')
        """
        return cls.random_element(cls.estados)

    @classmethod
    def estado_nome(cls):
        """
        Randomly returns a Brazilian State Name
        :example 'Minas Gerais'
        """
        return cls.estado()[1]

    @classmethod
    def estado_sigla(cls):
        """
        Randomly returns the abbreviation of a Brazilian State
        :example 'MG'
        """
        return cls.estado()[0]

    @classmethod
    def bairro(cls):
        """
        Randomly returns a bairro (neighborhood) name. The names were taken from the city of Belo Horizonte - Minas Gerais
        :example 'Serra'
        """
        return cls.random_element(cls.bairros)


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
