# coding: utf-8
from django.test import TestCase
from subscriptions.forms import SubscriptionForm


class SubscriptionsFormTest(TestCase):
    def test_form_has_fields(self):
        """ Form must contains fields.  """
        form = SubscriptionForm()
        self.assertItemsEqual(
            ['name', 'cpf', 'email', 'phone'], form.fields)
