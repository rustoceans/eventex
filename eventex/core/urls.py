# coding: utf-8
from django.conf.urls import patterns, url


urlpatterns = patterns('eventex.core.views',
    url(r'^$', 'home', name='home'),
    url(r'^palestrantes/(?P<slug>[\w-]+)/$', 'speaker_detail',
        name='speaker_detail'),
    url(r'^palestrantes/$', 'talk_list', name='talk_list')
)
