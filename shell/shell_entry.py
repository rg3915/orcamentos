import random
import rstr
from core.models import Entry, Category, Work, Person, Seller

priority_list = (
    ('u'),
    ('a'),
    ('n'),
    ('b'),
)

REPEAT = 40

for i in range(1, REPEAT + 1):
    priority = random.choice(priority_list)
    c = random.randint(1, 8)
    category = Category.objects.get(pk=c)
    work = Work.objects.get(pk=i)
    p = random.randint(1, 50)
    person = Person.objects.get(pk=p)
    s = random.randint(1, 3)
    seller = Seller.objects.get(pk=s)
    # regular expressions
    description = rstr.rstr(rstr.xeger(r'[\w]+'), 10, 20)
    Entry.objects.create(
        priority=priority,
        category=category,
        work=work,
        person=person,
        description=description,
        seller=seller,
    )

print('%d Entrys salvo com sucesso.' % REPEAT)
