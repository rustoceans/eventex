# coding: utf-8
from django.test import TestCase
from django.core.exceptions import ValidationError
from eventex.core.models import Talk, Media


class MediaModelTest(TestCase):

    def setUp(self):
        talk = Talk.objects.create(title='Talk', start_time='10:00')
        self.media = Media.objects.create(talk=talk, kind='YT', title='Video',
                                          media_id='QjA5faZF1A8')

    def test_create(self):
        self.assertEquals(1, self.media.pk)

    def test_unicode(self):
        self.assertEquals(u'Talk - Video', unicode(self.media))

    def test_kinf(self):
        media = Media(talk_id=1, kind='IM',
                      title='Video', media_id='QjA5faZF1A8')
        self.assertRaises(ValidationError, media.full_clean)
