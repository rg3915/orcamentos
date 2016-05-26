from django.utils import timezone
from django.core.management.base import BaseCommand
from orcamentos.proposal.models import Proposal


class Command(BaseCommand):
    help = ''' Preenche a data de orçamento sem data. '''

    def handle(self, *args, **kwargs):
        Proposal.objects.filter(created_orc=None).update(
            created_orc=timezone.now())

        print('Orçamentos atualizados com sucesso')
