from django.test import TestCase
from django.shortcuts import resolve_url as r
from orcamentos.proposal.models import Entry
from .test_base import BaseEntryTest


class EntryDetailGet(BaseEntryTest, TestCase):

    def setUp(self):
        super(EntryDetailGet, self).setUp()
        self.resp = self.client.get(r('proposal:entry_detail', 1))

    def test_create(self):
        self.assertTrue(Entry.objects.exists())

    def test_get(self):
        ''' GET shuld return status 200 '''
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'proposal/entry_detail.html')


class EntryDetailNotFound(TestCase):

    def test_not_found(self):
        response = self.client.get(r('proposal:entry_detail', 0))
        self.assertEqual(404, response.status_code)
