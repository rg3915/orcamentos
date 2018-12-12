from django.test import TestCase
from django.shortcuts import resolve_url as r
from orcamentos.crm.models import Person
from .data import PERSON_DICT


class PersonDetailGet(TestCase):

    def setUp(self):
        self.obj = Person.objects.create(**PERSON_DICT)
        self.resp = self.client.get(
            r('crm:person_detail', slug='regis-da-silva'))

    def test_get(self):
        ''' GET shuld return status 200 '''
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'crm/person_detail.html')

    def test_html(self):
        contents = [
            (1, 'Editar'),
        ]

        for count, expected in contents:
            with self.subTest():
                self.assertContains(self.resp, expected, count)

    def test_context(self):
        ''' Person must be in context '''
        person = self.resp.context['person']
        self.assertIsInstance(person, Person)


class PersonDetailNotFound(TestCase):

    def test_not_found(self):
        response = self.client.get(r('crm:person_detail', slug='not-found'))
        self.assertEqual(404, response.status_code)
