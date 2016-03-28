import json
from django.db.models import Count
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, JsonResponse
from .models import Proposal, Contract


def proposal_per_status_json(request):
    ''' JSON used to generate the graphic '''
    ''' Quantidade de orçamentos por status '''
    data = Proposal.objects.values('status')\
        .annotate(value=Count('status'))\
        .order_by('status').values('status', 'value')
    '''
    Precisa reescrever o dicionário com os campos do gráfico,
    que são: 'label' e 'value'.
    '''
    data = [{'label': x['status'], 'value':x['value']} for x in data]
    s = json.dumps(list(data), cls=DjangoJSONEncoder)
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
