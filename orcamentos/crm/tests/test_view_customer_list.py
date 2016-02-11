from django.test import TestCase
from django.shortcuts import resolve_url as r
from orcamentos.crm.models import Customer
from .data import CUSTOMER_DICT


class CustomerListGet(TestCase):

    def setUp(self):
        self.obj = Customer.objects.create(**CUSTOMER_DICT)
        self.resp = self.client.get(r('crm:customer_list'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'crm/customer_list.html')

    def test_html(self):
        contents = [
            (1, 'Adicionar'),
        ]

        for count, expected in contents:
            with self.subTest():
                self.assertContains(self.resp, expected, count)

    # def test_html(self):
    #     contents = [
    #         (1, 'Mike Smith'),
    #         (1, CUSTOMER_DICT['email']),
    #         (1, CUSTOMER_DICT['company']),
    #         (1, CUSTOMER_DICT['department']),
    #         (1, 'arquitetura'),
    #     ]

    #     for count, expected in contents:
    #         with self.subTest():
    #             self.assertContains(self.resp, expected, count)

    def test_context(self):
        variables = ['customer_list']

        for key in variables:
            with self.subTest():
                self.assertIn(key, self.resp.context)

    def test_full_name(self):
        ''' Must have full name '''
        expected = ' '.join(filter(None, ['Arq.', CUSTOMER_DICT[
                            'first_name'], CUSTOMER_DICT['last_name']]))
        self.assertEqual(expected, self.obj.full_name)


class CustomerListGetEmpty(TestCase):

    def test_get_empty(self):
        response = self.client.get(r('crm:customer_list'))

        self.assertContains(response, 'Sem itens na lista.')
