# coding: utf-8
from django.test import TestCase
from subscriptions.forms import SubscriptionForm


class SubscriptionsFormTest(TestCase):
    def test_form_has_fields(self):
        """ Form must contains fields.  """
        form = SubscriptionForm()
        self.assertItemsEqual(['name', 'cpf', 'email', 'phone'], form.fields)

    def test_cpf_is_digit(self):
        """ CPF must have digits. """
        form = self.test_make_validated_form(cpf='BA3434ADFA')
        self.assertItemsEqual(['cpf'], form.errors)

    def test_cpf_has_11_digits(self):
        """ CPF must have 11 digits. """
        form = self.test_make_validated_form(cpf='1234')
        self.assertItemsEqual(['cpf'], form.errors)

    def test_email_is_optional(self):
        """ E-mail is optional """
        form = self.test_make_validated_form(email='')
        self.assertFalse(form.errors)

    def test_make_validated_form(self, **kwargs):
        data = dict(name='Matheus Oliveira', cpf='36462297808',
                    email='oliveira.matheusde@gmail.com', phone='(16)98170033')
        data.update(kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form
