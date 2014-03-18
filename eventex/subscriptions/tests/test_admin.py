# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.admin import SubscriptionAdmin, Subscription, admin
from mock import Mock


class MarkAsPaidTest(TestCase):
    def setUp(self):
        # Instância do model admin
        self.model_admin = SubscriptionAdmin(Subscription, admin.site)
        Subscription.objects.create(name='Matheus', cpf='99999999999',
                                    email='matheu@coder42.com')

    def test_has_action(self):
        """ Action is installed """
        self.assertIn('mark_as_paid', self.model_admin.actions)

    def test_mark_all_paid(self):
        """ Mark all as paid """
        fake_request = Mock()
        queryset = Subscription.objects.all()
        self.model_admin.mark_as_paid(fake_request, queryset)

        self.assertEquals(1, Subscription.objects.filter(paid=True).count())
