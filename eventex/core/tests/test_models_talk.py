# coding: utf-8
from django.test import TestCase
from eventex.core.models import Talk


class TestModelTalk(TestCase):
    def setUp(self):
        self.talk = Talk.objects.create(
            title=u'Introdução ao Django',
            description=u'Descrição da palestra',
            start_time='10:00')

    def test_create(self):
        self.assertEquals(1, self.talk.pk)

    def test_unicode(self):
        self.assertEquals(u'Introdução ao Django', unicode(self.talk))

    def test_speakers(self):
        self.talk.speakers.create(name=u'Matheus Oliveira',
                                  slug=u'matheus-oliveira',
                                  url='http://coder42.com/')
        self.assertEquals(1, self.talk.speakers.count())
