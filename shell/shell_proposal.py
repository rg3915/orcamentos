from random import randint, choice
from django.utils import timezone
from orcamentos.crm.models import Person, Employee, Seller
from orcamentos.proposal.models import Proposal, Work, NumLastProposal
from orcamentos.utils.gen_random_values import gen_string, gen_decimal

status_list = ('c', 'elab', 'p', 'co')

REPEAT = 60

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

for i in range(1, REPEAT + 1):
    c = randint(1, 8)
    description = gen_string(30)
    w = randint(min_work_pk, max_work_pk)
    work = Work.objects.get(pk=w)
    # obtem todos os pk de contatos
    person_pks = [pk[0] for pk in Person.objects.all().values_list('pk')]
    p = choice(person_pks)
    person = Person.objects.get(pk=p)
    # obtem todos os pk de funcionários
    employee_pks = [pk[0] for pk in Employee.objects.all().values_list('pk')]
    e = choice(employee_pks)
    employee = Employee.objects.get(pk=e)
    # obtem todos os pk de vendedores
    seller_pks = [pk[0] for pk in Seller.objects.all().values_list('pk')]
    s = choice(seller_pks)
    seller = Seller.objects.get(pk=s)
    # escolhe um status
    status = choice(status_list)
    if status == 'co':
        date_conclusion = timezone.now()
        price = gen_decimal(9, 2)
    else:
        date_conclusion = None
        price = 0
    obj = Proposal(
        num_prop=i,
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

if not NumLastProposal.objects.all().count():
    NumLastProposal.objects.create(num_last_prop=0)

num_last_proposal = NumLastProposal.objects.get(pk=1)
num_last_proposal.num_last_prop = REPEAT
num_last_proposal.save()
