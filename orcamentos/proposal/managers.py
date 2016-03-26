from django.db import models


class EntryManager(models.Manager):
    ''' Entrada é todo orçamento com num_prop = 0 '''

    def get_queryset(self):
        return super(EntryManager, self).get_queryset().filter(num_prop=0)


class ProposalManager(models.Manager):
    ''' Orçamento é todo orçamento com num_prop > 0 '''

    def get_queryset(self):
        return super(ProposalManager, self).get_queryset().filter(num_prop__gt=0)
