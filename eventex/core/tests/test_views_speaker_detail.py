# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r
from eventex.core.models import Speaker


class SpeakerDetailTest(TestCase):

    """
    Run tests of speaker_detail
    """

    def setUp(self):
        Speaker.objects.create(
            name='Matheus Oliveira',
            slug='matheus-oliveira',
            url='http://coder42.com/',
            description='Passionate software developer!')

        url = r('core:speaker_detail', kwargs={'slug': 'matheus-oliveira'})
        self.resp = self.client.get(url)

    def test_get(self):
        """ GET should be result in 200 """
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """ Template should be core/speaker_detail.html """
        self.assertTemplateUsed(self.resp, 'core/speaker_detail.html')

    def test_html(self):
        """ Html must contain data. """
        self.assertContains(self.resp, 'Matheus Oliveira')
        self.assertContains(self.resp, 'Passionate software developer!')
        self.assertContains(self.resp, 'http://coder42.com/')

    def test_context(self):
        """ Speaker must be in context. """
        speaker = self.resp.context['speaker']

        self.assertIsInstance(speaker, Speaker)


class SpeakerDetailNotFoundTest(TestCase):

    def test_not_found(self):
        url = r('core:speaker_detail', kwargs={'slug': 'john-jones'})
        response = self.client.get(url)
        self.assertEquals(404, response.status_code)
