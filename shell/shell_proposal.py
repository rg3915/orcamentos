import random
import rstr
from core.models import Proposal, Category, Work, Person, Employee, Seller, NumLastProposal
from shell.gen_random_values import gen_date, gen_decimal

# eu quis ordenar alguns status de propósito
status_list = (
    ('elab'),
    ('p'),
    ('c'),
    ('co'),
    ('elab'),
    ('c'),
    ('co'),
    ('p'),
    ('a'),
    ('a'),
)

REPEAT = 10

for i in range(1, REPEAT + 1):
    c = random.randint(1, 8)
    category = Category.objects.get(pk=c)
    description = rstr.rstr(rstr.xeger(r'[\w]+'), 10, 20)
    w = random.randint(1, 40)
    work = Work.objects.get(pk=w)
    p = random.randint(1, 50)
    person = Person.objects.get(pk=p)
    e = random.randint(1, 9)
    employee = Employee.objects.get(pk=e)
    s = random.randint(1, 3)
    seller = Seller.objects.get(pk=s)
    status = status_list[i - 1]
    if status == 'co' or status == 'a':
        date_conclusion = gen_date(min_year=2015, max_year=2015)
        price = gen_decimal(9, 2)
    else:
        date_conclusion = None
        price = 0
    obj = Proposal(
        num_prop=i,
        type_prop='R',
        num_type_prop=0,
        category=category,
        description=description,
        work=work,
        person=person,
        employee=employee,
        seller=seller,
        status=status,
        date_conclusion=date_conclusion,
        price=price,
    )
    obj.save()

num_last_proposal = NumLastProposal.objects.get(pk=1)
num_last_proposal.num_last_prop = REPEAT
num_last_proposal.save()
print('%d Proposals salvo com sucesso.' % REPEAT)
