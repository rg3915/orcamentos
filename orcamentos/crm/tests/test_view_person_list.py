from django.test import TestCase
from django.shortcuts import resolve_url as r
from orcamentos.crm.models import Person
from .data import PERSON_DICT


class PersonListGet(TestCase):

    def setUp(self):
        self.obj = Person.objects.create(**PERSON_DICT)
        self.resp = self.client.get(r('crm:person_list'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'crm/person_list.html')

    def test_html(self):
        contents = [
            (1, 'Adicionar'),
        ]

        for count, expected in contents:
            with self.subTest():
                self.assertContains(self.resp, expected, count)

    def test_context(self):
        variables = ['person_list']

        for key in variables:
            with self.subTest():
                self.assertIn(key, self.resp.context)

    def test_full_name(self):
        ''' Must have full name '''
        expected = ' '.join(filter(None, ['Sr.', PERSON_DICT[
                            'first_name'], PERSON_DICT['last_name']]))
        self.assertEqual(expected, self.obj.full_name)


class PersonListGetEmpty(TestCase):

    def test_get_empty(self):
        response = self.client.get(r('crm:person_list'))

        self.assertContains(response, 'Sem itens na lista.')
