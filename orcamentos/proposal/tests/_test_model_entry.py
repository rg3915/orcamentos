from datetime import datetime
from django.shortcuts import resolve_url as r
from django.test import TestCase
from orcamentos.proposal.models import Entry
from .test_base import BaseEntryTest


class EntryTest(BaseEntryTest, TestCase):

    def test_create(self):
        self.assertTrue(Entry.objects.exists())

    def test_created(self):
        ''' Entry must have an auto created attr. '''
        self.assertIsInstance(self.obj.created, datetime)

    def test_str(self):
        self.assertEqual('Ed. Atlanta', str(self.obj))

    def test_ordering(self):
        self.assertListEqual(['priority', 'created'], Entry._meta.ordering)

    def test_get_absolute_url(self):
        url = r('proposal:entry_detail', pk=self.obj.pk)
        self.assertEqual(url, self.obj.get_absolute_url())
