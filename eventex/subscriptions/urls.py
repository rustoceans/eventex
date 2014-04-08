# coding: utf-8
from django.conf.urls import patterns, url


urlpatterns = patterns('eventex.subscriptions.views',
    url(r'^(\d+)/$', 'detail', name='detail'),
    url(r'^$', 'subscribe', name='subscribe'),
)
