# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r
from eventex.subscriptions.models import Subscription


class DetailTest(TestCase):
    def setUp(self):
        s = Subscription.objects.create(
            name='Matheus Oliveira',
            cpf='364.622.978-08',
            email='matheus@coder42.com',
            phone='(16) 98170-0339')
        self.resp = self.client.get(r('subscriptions:detail', args=[1]))

    def test_get(self):
        """ GET /inscricao/1/ should be return status 200. """
        self.assertEquals(200, self.resp.status_code)

    def test_template(self):
        """ Uses template. """
        self.assertTemplateUsed(
            self.resp, 'subscriptions/subscription_detail.html')

    def test_context(self):
        """ Context must have a subscription instance. """
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        """ Check if subscription data was rendered. """
        self.assertContains(self.resp, 'Matheus Oliveira')


class DetailNotFoundTest(TestCase):
    def test_not_found(self):
        """ Subscription Not found. """
        response = self.client.get(r('subscriptions:detail', args=[0]))

        self.assertEquals(404, response.status_code)
