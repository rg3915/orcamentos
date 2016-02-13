from django.utils import timezone

USER_DICT = {
    'username': 'regis',
    'first_name': 'Regis',
    'last_name': 'da Silva',
    'email': 'regis@example.com',
    'password': 'demodemo',
}

PERSON_DICT = {
    'gender': 'M',
    'treatment': 'sr',
    'first_name': 'Regis',
    'last_name': 'da Silva',
    'slug': 'regis-da-silva',
    'birthday': '1985-12-01 02:42:30+00:00',
    'company': 'Acme',
    'department': 'Tecnologia',
    'email': 'regis@example.com',
    'cpf': '75873211795',
    'rg': '911225341',
    'address': u'Rua São Leopoldo, 101',
    'complement': 'Apto 303',
    'district': u'Belezinho',
    'city': u'São Paulo',
    'uf': 'SP',
    'cep': '03055000',
    'active': True,
    'blocked': False,
}

CUSTOMER_DICT = {
    'gender': 'M',
    'treatment': 'a',
    'first_name': 'Mike',
    'last_name': 'Smith',
    'slug': 'mike-smith',
    'birthday': '1942-06-01 00:00:01+00:00',
    'company': 'Thompson',
    'department': u'Arquitetura',
    'email': 'm.smith@example.com',
    'cpf': '92563474663',
    'rg': '403289440',
    'cnpj': '42238377000123',
    'ie': 'isento',
    'customer_type': 'a',
    'address': 'Avenida Paulista, 1605',
    'complement': 'Apto 42',
    'district': 'Bela Vista',
    'city': u'São Paulo',
    'uf': 'SP',
    'cep': '01311200',
    'active': True,
    'blocked': False,
}

EMPLOYEE_DICT = {
    'gender': 'M',
    'treatment': 'sr',
    'slug': 'regis',
    'company': 'Acme',
    'department': 'Tecnologia',
    'cpf': '28586897337',
    'rg': '418757896',
    'address': u'Rua Rafael Barbosa',
    'complement': '15º andar',
    'district': u'Vila Andradina',
    'city': u'Goiás',
    'uf': 'GO',
    'cep': '74665841',
    'active': True,
    'date_entry': timezone.now(),
    'date_release': timezone.now(),
}

SELLER_DICT = {
    'internal': True,
    'commissioned': True,
    'commission': 0.01,
}
