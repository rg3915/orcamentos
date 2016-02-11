from django.shortcuts import resolve_url as r
from django.test import TestCase
from .test_base import BaseProposalTest


class ProposalListGet(BaseProposalTest, TestCase):

    def setUp(self):
        self.resp = self.client.get(r('proposal:proposal_list'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'proposal/proposal_list.html')

    def test_context(self):
        variables = ['proposal_list']

        for key in variables:
            with self.subTest():
                self.assertIn(key, self.resp.context)


class ProposalListGetEmpty(TestCase):

    def test_get_empty(self):
        response = self.client.get(r('proposal:proposal_list'))

        self.assertContains(response, 'Sem itens na lista.')
