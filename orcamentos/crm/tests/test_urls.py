from django.shortcuts import resolve_url as r
from django.test import TestCase
from django.test.client import Client


# path('', c.PersonList.as_view(), name='person_list'),
# path('<slug>/', c.person_detail, name='person_detail'),


class UrlTest(TestCase):

    def test_urls_contract(self):
        urls = (
            {
                'url': '/crm/person/',
                'name': 'person_list',
            },
        )

        for url in urls:
            with self.subTest():
                self.r = self.client.get(url['url'])
                self.assertEqual(200, self.r.status_code)
                self.r = self.client.get(r('crm:{}'.format(url['name'])))
                self.assertEqual(200, self.r.status_code)
