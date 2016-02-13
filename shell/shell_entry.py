from random import randint, choice
from shell.gen_random_values import gen_string
from orcamentos.core.models import Entry, Category, Work, Person, Seller
from orcamentos.core.lists import URGENTE, ALTA, NORMAL, BAIXA

priority_list = ((URGENTE), (ALTA), (NORMAL), (BAIXA))

# Return min id of work
try:
    min_work_pk = Work.objects.order_by('pk')[0].pk
except IndexError:
    min_work_pk = None

# Return max id of work
try:
    max_work_pk = Work.objects.latest('pk').id
except Work.DoesNotExist:
    max_work_pk = None

REPEAT = max_work_pk + 1

for i in range(min_work_pk, REPEAT):
    priority = choice(priority_list)
    c = randint(1, 8)
    category = Category.objects.get(pk=c)
    work = Work.objects.get(pk=i)
    p = randint(1, 50)
    person = Person.objects.get(pk=p)
    s = randint(1, 3)
    seller = Seller.objects.get(pk=s)
    description = gen_string(30)
    Entry.objects.create(
        priority=priority,
        category=category,
        work=work,
        person=person,
        description=description,
        seller=seller,
    )

print('%d Entrys salvo com sucesso.' % REPEAT)
