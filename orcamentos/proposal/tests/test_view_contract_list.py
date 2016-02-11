from django.test import TestCase
from django.shortcuts import resolve_url as r
from .test_base import BaseContractTest


class ContractListGet(BaseContractTest, TestCase):

    def setUp(self):
        self.resp = self.client.get(r('proposal:contract_list'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'proposal/contract_list.html')

    def test_context(self):
        variables = ['contract_list']

        for key in variables:
            with self.subTest():
                self.assertIn(key, self.resp.context)


class ContractListGetEmpty(TestCase):

    def test_get_empty(self):
        response = self.client.get(r('proposal:contract_list'))
        self.assertContains(response, 'Sem itens na lista.')
