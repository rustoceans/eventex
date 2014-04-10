# coding: utf-8
from django.conf.urls import patterns, url
from .views import HomeView, SpeakerDetail, TalkDetail


urlpatterns = patterns('eventex.core.views',
    url(r'^palestrantes/(?P<slug>[\w-]+)/$', SpeakerDetail.as_view(),
        name='speaker_detail'),
    url(r'^palestras/(?P<pk>\d+)/$', TalkDetail.as_view(), name='talk_detail'),
    url(r'^palestras/$', 'talk_list', name='talk_list'),
    url(r'^$', HomeView.as_view(), name='home')
)
