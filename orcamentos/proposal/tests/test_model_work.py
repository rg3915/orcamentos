from django.shortcuts import resolve_url as r
from django.test import TestCase
from orcamentos.proposal.models import Work
from .test_base import BaseWorkTest


class WorkTest(BaseWorkTest, TestCase):

    def test_create(self):
        self.assertTrue(Work.objects.exists())

    def test_str(self):
        self.assertEqual('Ed. Atlanta', str(self.obj))

    def test_ordering(self):
        self.assertListEqual(['name_work'], Work._meta.ordering)

    def test_get_absolute_url(self):
        url = r('proposal:work_detail', slug=self.obj.slug)
        self.assertEqual(url, self.obj.get_absolute_url())
