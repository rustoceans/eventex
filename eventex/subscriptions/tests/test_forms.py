# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionsFormTest(TestCase):
    def test_form_has_fields(self):
        """ Form must contains fields.  """
        form = SubscriptionForm()

        self.assertItemsEqual(['name', 'cpf', 'email', 'phone'], form.fields)

    def test_cpf_is_digit(self):
        """ CPF must have digits. """
        form = self.make_validated_form(cpf='BA3434ADFA')

        self.assertItemsEqual(['cpf'], form.errors)

    def test_cpf_has_11_digits(self):
        """ CPF must have 11 digits. """
        form = self.make_validated_form(cpf='1234')

        self.assertItemsEqual(['cpf'], form.errors)

    def test_email_is_optional(self):
        """ E-mail is optional """
        form = self.make_validated_form(email='')

        self.assertFalse(form.errors)

    def test_name_must_be_capitalize(self):
        """ Name must be capitalize """
        form = self.make_validated_form(name='MATHEUS oliveira')

        self.assertEquals('Matheus Oliveira', form.cleaned_data['name'])

    def test_must_inform_email_or_phone(self):
        """ Email or Phone are optional, but one must be informed. """
        form = self.make_validated_form(email='', phone_0='', phone_1='')

        self.assertItemsEqual(['__all__'], form.errors)

    def make_validated_form(self, **kwargs):
        data = dict(name='Matheus Oliveira', cpf='36462297808',
                    email='oliveira.matheusde@gmail.com',
                    phone_0='16', phone_1='98170033')
        data.update(kwargs)
        form = SubscriptionForm(data)
        form.is_valid()

        return form
