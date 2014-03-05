# coding: utf-8
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from .models import Subscription


def cpf_validator(value):
    if not value.isdigit():
        raise ValidationError(_(u'CPF deve conter apenas números.'))
    if not len(value) is 11:
        raise ValidationError(_(u'CPF deve conter 11 dígitos'))


class SubscriptionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SubscriptionForm, self).__init__(*args, **kwargs)

        self.fields['cpf'].validators.append(cpf_validator)

    class Meta:
        model = Subscription
        fields = ('name', 'cpf', 'email', 'phone')
