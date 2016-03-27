import json
from django.db.models import Count
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from .models import Proposal


def proposal_per_status_json(request):
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
