import json
import itertools
from django.db.models import Count
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, JsonResponse
from .models import Proposal, Contract
from orcamentos.utils.lists import STATUS_LIST

STATUS_DICT = dict(STATUS_LIST)


def proposal_per_status_json(request):
    ''' JSON used to generate the graphic '''
    ''' Quantidade de orçamentos por status '''
    data = Proposal.objects.values('status')\
        .annotate(value=Count('status'))\
        .order_by('status').values('status', 'value')
    '''
    Precisa reescrever o dicionário com os campos do gráfico,
    que são: 'label' e 'value'. E ainda retornar o get_status_display.
    '''
    lista = [{'label': STATUS_DICT[item['status']],
              'value': item['value']} for item in data]
    s = json.dumps(lista, cls=DjangoJSONEncoder)
    return HttpResponse(s)


def count_contract_aproved():
    return Contract.objects.filter(is_canceled=False).count()


def get_data(is_aproved, is_canceled):
    data = [{'label': 'Aprovados', 'value': is_aproved},
            {'label': 'Cancelados', 'value': is_canceled}]
    return data


def contract_aprov_canceled_json(request):
    ''' JSON used to generate the graphic '''
    ''' Quantidade de contratos aprovados x cancelados '''
    total = Contract.objects.count()
    is_aproved = count_contract_aproved()
    is_canceled = total - is_aproved
    resp = JsonResponse(get_data(is_aproved, is_canceled), safe=False)
    return HttpResponse(resp.content)


def contract_more_expensive_json(request):
    ''' 5 contratos mais caros '''
    c = Contract.objects.all().values(
        'proposal__work__name_work',
        'proposal__price').order_by('-proposal__price')[:5]
    s = json.dumps(list(c), cls=DjangoJSONEncoder)
    return HttpResponse(s)


def contract_total_per_month_json(request):
    ''' valor total fechado por mês no ano '''
    c = Contract.objects.all().values('created', 'proposal__price') \
        .filter(is_canceled=False)
    gr = itertools.groupby(c, lambda d: d.get('created').strftime('%Y-%m'))
    dt = [{'month': month, 'total': sum(
        [x['proposal__price'] for x in total])} for month, total in gr]
    s = json.dumps(list(dt), cls=DjangoJSONEncoder)
    return HttpResponse(s)
