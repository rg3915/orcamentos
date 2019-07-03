from django.contrib.auth.models import User
from django.shortcuts import resolve_url as r
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse_lazy as rl
from orcamentos.crm.models import Person


class UrlTest(TestCase):

    def setUp(self):
        self.credentials = dict(username='regis', password='demodemo')
        self.user = User.objects.create_user(**self.credentials)
        self.login = self.client.force_login(self.user)
        self.resp = self.client.get(r('crm:person_list'))
        # Cria Person
        self.person = Person.objects.create(
            gender='I',
            first_name='regis',
            last_name='santos',
            slug='regis-santos',
            person_type='p',
        )

    def test_urls_contract(self):
        urls = (
            {
                'url': '/crm/person/',
                'name': 'person_list',
            },
            {
                'url': '/crm/person/{}/'.format(self.person.slug),
                'name': 'person_detail',
                'slug': self.person.slug,
            },
        )

        for url in urls:
            with self.subTest():
                self.r = self.client.get(url['url'])
                self.assertEqual(200, self.r.status_code)
                self._url = 'crm:{}'.format(url['name'])
                if url.get('slug'):
                    kw = {'slug': self.person.slug}
                    self.r = self.client.get(rl(self._url, kwargs=kw))
                else:
                    self.r = self.client.get(rl(self._url))
                self.assertEqual(200, self.r.status_code)
