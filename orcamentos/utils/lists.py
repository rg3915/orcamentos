# -*- coding: utf-8 -*-
GENDER = (
    ('I', 'não informado'),
    ('M', 'masculino'),
    ('F', 'feminino')
)

TREATMENT = (
    ('a', 'Arq.'),
    ('aa', 'Arqa.'),
    ('d', 'Dona'),
    ('dr', 'Dr.'),
    ('dra', 'Dra.'),
    ('e', 'Eng.'),
    ('ea', u'Engª.'),
    ('p', 'Prof.'),
    ('pa', 'Profa.'),
    ('sr', 'Sr.'),
    ('sra', 'Sra.'),
    ('srta', 'Srta.'),
)

PHONE_TYPE = (
    ('pri', 'principal'),
    ('com', 'comercial'),
    ('res', 'residencial'),
    ('cel', 'celular'),
    ('cl', 'Claro'),
    ('oi', 'Oi'),
    ('t', 'Tim'),
    ('v', 'Vivo'),
    ('n', 'Nextel'),
    ('fax', 'fax'),
    ('o', 'outros'),
)

CUSTOMER_TYPE = (
    ('c', 'construtora'),
    ('a', 'arquitetura'),
    ('p', 'particular')
)

PERSON_TYPE = (
    ('c', 'cliente'),
    ('p', 'contato'),
)

URGENTE = 'a1'
ALTA = 'a2'
NORMAL = 'a3'
BAIXA = 'a4'
PRIORITY = (
    (URGENTE, 'Urgente'),
    (ALTA, 'Alta'),
    (NORMAL, 'Normal'),
    (BAIXA, 'Baixa'),
)

PROP_TYPE = (
    ('R', 'R'),
    ('OP', 'OP')
)

STATUS_FILTER = (
    ('c', 'cancelado'),
    ('elab', 'em elaboração'),
    ('p', 'pendente'),
    ('co', 'concluido'),
    ('a', 'aprovado')
)

STATUS_LIST = (
    ('c', 'cancelado'),
    ('n', 'não iniciado'),
    ('elab', 'em elaboração'),
    ('p', 'pendente'),
    ('co', 'concluido'),
    ('a', 'aprovado')
)

CATEGORY = (
    ('orc', 'orçamento'),
    ('cc', 'concorrência'),
    ('cn', 'consulta'),
    ('ct', 'cotação'),
    ('e', 'extra'),
    ('g', 'global'),
    ('p', 'particular'),
    ('ou', 'outros'),
)

OCCUPATION_LIST = (
    u'Arquiteto',
    u'Coordenador',
    u'Diretor',
    u'Engenheiro',
    u'Estagiário',
    u'Gerente',
    u'Orçamentista',
    u'Vendedor',
)

COMPANY_LIST = (
    ('Acme'),
    ('Cyberdyne'),
    ('Ghostbusters'),
    ('Globex'),
    ('Gringotes'),
    ('ILM'),
    ('Oscorp'),
    ('RG Solutions'),
    ('Stark'),
    ('Tabajara'),
    ('Teknotronic'),
    ('Tivit'),
    ('Wayne'),
    ('Wonka'),
)
