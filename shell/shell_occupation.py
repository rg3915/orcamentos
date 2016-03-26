from orcamentos.crm.models import Occupation
from orcamentos.utils.lists import OCCUPATION_LIST

obj = [Occupation(occupation=val) for val in OCCUPATION_LIST]
Occupation.objects.bulk_create(obj)
