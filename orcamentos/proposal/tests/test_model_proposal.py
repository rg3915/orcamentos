from datetime import datetime
from django.shortcuts import resolve_url as r
from django.test import TestCase
from orcamentos.proposal.models import Proposal
from .test_base import BaseProposalTest


class ProposalTest(BaseProposalTest, TestCase):

    def test_create(self):
        self.assertTrue(Proposal.objects.exists())

    def test_created(self):
        ''' Proposal must have an auto created attr. '''
        self.assertIsInstance(self.obj.created, datetime)

    def test_str(self):
        # Format expected 001.15.0
        actual_year = datetime.now().strftime('%y')
        self.assertEqual('001.{}.0'.format(actual_year), str(self.obj))

    def test_ordering(self):
        self.assertListEqual(['id'], Proposal._meta.ordering)

    def test_get_absolute_url(self):
        url = r('proposal:proposal_detail', pk=self.obj.pk)
        self.assertEqual(url, self.obj.get_absolute_url())
