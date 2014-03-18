# coding: utf-8
from django.contrib import admin
from django.utils.translation import ungettext, ugettext_lazy as _
from django.utils.datetime_safe import datetime
from .models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'cpf', 'phone',
                    'created_at', 'subscribed_today', 'paid',)
    date_hierarchy = 'created_at'
    search_fields = ('name', 'email', 'cpf', 'phone', 'created_at')
    list_filter = ('created_at',)

    def subscribed_today(self, obj):
        return obj.created_at.date() == datetime.now().date()
    subscribed_today.short_description = _('inscrito hoje?')
    subscribed_today.boolean = True
    actions = ['mark_as_paid']

    def mark_as_paid(self, request, queryset):
        count = queryset.update(paid=True)
        message = ungettext(
            u'%d inscrição foi marcada como paga.',
            u'%d inscrições foram marcadas como pagas.',
            count
        )
        self.message_user(request, message % count)

    mark_as_paid.short_description = _('Marcar como pago')


# Register model in admin site
admin.site.register(Subscription, SubscriptionAdmin)
