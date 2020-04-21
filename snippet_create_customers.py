import names
from random import choice
from django.template.defaultfilters import slugify
from orcamentos.crm.models import Customer


CUSTOMERTYPES = ('c', 'a', 'p')
DEPARTMENTS = (
    'Financeiro',
    'Jurídico',
    'Recursos Humanos',
    'Tecnologia',
    'Vendas',
)

aux = []
for i in range(200):
    customer_type = choice(CUSTOMERTYPES)
    first_name = names.get_first_name()
    last_name = names.get_last_name()
    department = choice(DEPARTMENTS)
    slug = slugify('{} {}'.format(first_name, last_name))
    obj = Customer(
        person_type='c',
        customer_type=customer_type,
        first_name=first_name,
        last_name=last_name,
        department=department,
        slug=slug,
    )
    aux.append(obj)

Customer.objects.bulk_create(aux)


# Customer.objects.all().count()
