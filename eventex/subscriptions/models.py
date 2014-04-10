# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Subscription(models.Model):
    name = models.CharField(_('nome'), max_length=100)
    cpf = models.CharField(_('CPF'), max_length=11, unique=True)
    email = models.EmailField(_('e-mail'), blank=True)
    phone = models.CharField(_('telefone'), max_length=20, blank=True)
    paid = models.BooleanField(_('pago'), default=False)
    created_at = models.DateTimeField(_('criado em'), auto_now_add=True)

    class Meta:
        ordering = ['created_at']
        verbose_name = _(u'inscrição')
        verbose_name_plural = _(u'inscrições')

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('subscriptions:detail', (), dict(pk=self.pk))
