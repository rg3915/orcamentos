from django.test import TestCase
from orcamentos.proposal.models import NumLastProposal


class NumLastProposalTest(TestCase):

    def setUp(self):
        self.obj = NumLastProposal.objects.create(num_last_prop=1)

    def test_create(self):
        self.assertTrue(NumLastProposal.objects.exists())

    def test_str(self):
        self.assertEqual('1', str(self.obj))
