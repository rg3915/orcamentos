from django.utils import timezone

USER_DICT = {
    'username': 'regis',
    'first_name': 'Regis',
    'last_name': 'da Silva',
    'email': 'regis@example.com',
    'password': 'demodemo',
}

ENTRY_DICT = {
    'priority': 3,
    'category': 1,
    'description': 'Lorem ipsum dolor sit amet.',
    'is_entry': True,
}

PROPOSAL_DICT = {
    'num_prop': 1,
    'prop_type': 'R',
    'num_prop_type': 0,
    'category': 1,
    'description': 'Lorem ipsum dolor sit amet.',
    'date_conclusion': timezone.now(),
    'price': 9999.99,
    'obs': 'Lorem ipsum dolor sit amet.',
}

WORK_DICT = {
    'name_work': 'Ed. Atlanta',
    'slug': 'ed-atlanta',
    'address': u'Avenida Principal, 1001',
    'complement': '',
    'district': u'Itapuã',
    'city': u'São Paulo',
    'uf': 'SP',
    'cep': '04567200',
}
