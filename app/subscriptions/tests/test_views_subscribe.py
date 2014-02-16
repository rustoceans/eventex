# conding: utf-8
from django.test import TestCase
from subscriptions.forms import SubscriptionForm
from subscriptions.models import Subscription


class SubscribeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/inscricao/')

    def test_get(self):
        """ Get /inscricao/ must return status code 200. """
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """ Response should be a render template. """
        self.assertTemplateUsed(
            self.resp, 'subscriptions/subscription_form.html')

    def test_html(self):
        """ Html contains input control. """
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<label', 4)
        self.assertContains(self.resp, '<input', 6)
        self.assertContains(self.resp, 'type="text"', 3)
        self.assertContains(self.resp, 'type="email"')
        self.assertContains(self.resp, 'type="submit"')

    def test_csrf(self):
        """ Html must contain csrf token. """
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """ Context must have the subscription form. """
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)


class SubscribePostTest(TestCase):
    def setUp(self):
        data = dict(
            name='Matheus Oliveira', cpf='36462297808',
            email='oliveira.matheusde@gmail.com.br', phone='(16) 981700339')
        self.resp = self.client.post('/inscricao/', data)

    def test_post(self):
        """ Vaild POST should redirect to /inscricao/1 """
        self.assertEquals(302, self.resp.status_code)

    def test_save(self):
        """ Valid POST be saved """
        self.assertTrue(Subscription.objects.exists())


class SubscribeInvalidPostTest(TestCase):
    def setUp(self):
        data = dict(
            name='Matheus Oliveira', cpf='3646229780811',
            email='oliveira.matheusde@gmail.com.br', phone='(16) 981700339')
        self.resp = self.client.post('/inscricao/', data)

    def test_post(self):
        """ Invalid POST should not redirect. """
        self.assertEquals(200, self.resp.status_code)

    def test_form_errors(self):
        """ Form must contain errors. """
        self.assertTrue(self.resp.context['form'].errors)

    def test_dont_save(self):
        """ Do not save. """
        self.assertFalse(Subscription.objects.exists())