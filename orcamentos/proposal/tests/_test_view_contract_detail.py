from django.test import TestCase
from django.shortcuts import resolve_url as r
from orcamentos.proposal.models import Contract
from .test_base import BaseContractTest


class ContractDetailGet(BaseContractTest, TestCase):

    def setUp(self):
        super(ContractDetailGet, self).setUp()
        self.resp = self.client.get(r('proposal:contract_detail', 1))

    def test_create(self):
        self.assertTrue(Contract.objects.exists())

    def test_get(self):
        ''' GET shuld return status 200 '''
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'proposal/contract_detail.html')


class ContractDetailNotFound(TestCase):

    def test_not_found(self):
        response = self.client.get(r('proposal:contract_detail', 0))
        self.assertEqual(404, response.status_code)
