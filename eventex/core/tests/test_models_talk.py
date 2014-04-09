# coding: utf-8
from django.test import TestCase
from eventex.core.models import Talk, Course
from eventex.core.managers import PeriodManager


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

    def test_period_manager(self):
        """ Talk default manager must be instance of PeriodManager """
        self.assertIsInstance(Talk.objects, PeriodManager)


class CourseModelTest(TestCase):

    def setUp(self):
        self.course = Course.objects.create(title='Tutorial Django',
                                            description=u'Descrição do curso',
                                            start_time='10:00', slots=20)

    def test_create(self):
        self.assertEquals(1, self.course.pk)

    def test_unicode(self):
        self.assertEquals(u'Tutorial Django', unicode(self.course))

    def test_speakers(self):
        """ Course has many speakers and vice-versa """
        self.course.speakers.create(name='Matheus Oliveira',
                                    slug='matheus-oliveira',
                                    url='http:/coder42.com')
        self.assertEquals(1, self.course.speakers.count())

    def test_at_morning(self):
        """ Course default manager must be instance of PeriodManager """
        self.assertIsInstance(Course.objects, PeriodManager)
