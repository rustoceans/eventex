# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r
from eventex.core.models import Speaker, Talk


class TalkListTest(TestCase):

    def setUp(self):
        speaker = Speaker.objects.create(
            name='Matheus Oliveira',
            slug='matheus-oliveira',
            description='Passionate software developer!',
            url='http:/coder42.com/')
        t1 = Talk.objects.create(title=u'Título da palestra',
                                 description=u'Descrição da palestra',
                                 start_time='10:00')
        t2 = Talk.objects.create(title=u'Título da palestra',
                                 description=u'Descrição da palestra',
                                 start_time='13:00')
        speaker.talk_set.add(t1, t2)
        self.resp = self.client.get(r('core:talk_list'))

    def test_get(self):
        """ GET must result in 200 """
        self.assertEquals(200, self.resp.status_code)

    def test_template(self):
        """ Template should be core/talk_list.html """
        self.assertTemplateUsed(self.resp, 'core/talk_list.html')

    def test_html(self):
        """ HTML should list talks. """
        self.assertContains(self.resp, u'Título da palestra', 2)
        self.assertContains(self.resp, u'10:00')
        self.assertContains(self.resp, u'13:00')
        self.assertContains(self.resp, u'/palestras/1/')
        self.assertContains(self.resp, u'/palestras/2/')
        self.assertContains(self.resp, u'/palestrantes/matheus-oliveira/', 2)
        self.assertContains(self.resp, u'Passionate software developer!', 2)
        self.assertContains(self.resp, u'Matheus Oliveira', 2)
        self.assertContains(self.resp, u'Descrição da palestra', 2)

    def test_morning_talks_in_context(self):
        self.assertIn('morning_talks', self.resp.context)

    def test_afternoon_talks_in_context(self):
        self.assertIn('afternoon_talks', self.resp.context)
