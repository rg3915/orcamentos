from random import choice
from orcamentos.utils.gen_random_values import gen_string
from orcamentos.crm.models import Person, Seller
from orcamentos.proposal.models import Entry, Work
from orcamentos.utils.lists import URGENTE, ALTA, NORMAL, BAIXA

priority_list = (URGENTE, ALTA, NORMAL, BAIXA)

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
    work = Work.objects.get(pk=i)
    # obtem todos os pk de contatos
    person_pks = [pk[0] for pk in Person.objects.all().values_list('pk')]
    p = choice(person_pks)
    person = Person.objects.get(pk=p)
    # obtem todos os pk de vendedores
    seller_pks = [pk[0] for pk in Seller.objects.all().values_list('pk')]
    c = choice(seller_pks)
    seller = Seller.objects.get(pk=c)
    description = gen_string(30)
    obj = Entry(
        priority=priority,
        work=work,
        person=person,
        description=description,
        seller=seller,
    )
    obj.save()


# done
