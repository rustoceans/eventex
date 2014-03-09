# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Speaker(models.Model):
    name = models.CharField(_('nome'), max_length=255)
    slug = models.SlugField(_('slug'))
    url = models.URLField(_('url'))
    description = models.TextField(_(u'descrição'), blank=True)

    class Meta:
        verbose_name = _('palestrante')
        verbose_name_plural = _('palestrantes')

    def __unicode__(self):
        return self.name


class Contact(models.Model):
    KINDS = (
        ('P', _('Telefone')),
        ('F', _('Fax')),
        ('E', _('E-mail')),
    )

    speaker = models.ForeignKey('Speaker', verbose_name=_('palestrante'))
    kind = models.CharField(_('tipo'), max_length=1, choices=KINDS)
    value = models.CharField(_('valor'), max_length=255)

    class Meta:
        verbose_name = _('contato')
        verbose_name_plural = _('contatos')

    def __unicode__(self):
        return self.value
