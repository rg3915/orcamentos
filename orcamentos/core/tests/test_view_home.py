from django.test import TestCase
from django.shortcuts import resolve_url as r


class HomeTest(TestCase):

    def setUp(self):
        self.response = self.client.get(r('core:home'))

    def test_get(self):
        ''' GET / must return status code 200 '''
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        ''' Must use index.html '''
        self.assertTemplateUsed(self.response, 'index.html')

    def test_entry_link(self):
        expected = 'href="{}"'.format(r('core:entry_list'))
        self.assertContains(self.response, expected)

    def test_proposal_link(self):
        expected = 'href="{}"'.format(r('core:proposal_list'))
        self.assertContains(self.response, expected)

    def test_contract_link(self):
        expected = 'href="{}"'.format(r('core:contract_list'))
        self.assertContains(self.response, expected)

    def test_customer_link(self):
        expected = 'href="{}"'.format(r('core:customer_list'))
        self.assertContains(self.response, expected)

    def test_work_link(self):
        expected = 'href="{}"'.format(r('core:work_list'))
        self.assertContains(self.response, expected)

    def test_person_link(self):
        expected = 'href="{}"'.format(r('core:person_list'))
        self.assertContains(self.response, expected)
