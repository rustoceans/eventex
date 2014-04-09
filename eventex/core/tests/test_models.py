# coding: utf-8
from django.test import TestCase
from django.core.exceptions import ValidationError
from eventex.core.models import Speaker, Contact


class SpeakerModelTest(TestCase):

    def setUp(self):
        self.speaker = Speaker(name='Matheus Oliveira',
                               slug='matheus-oliveira',
                               url='http://coder42.com/',
                               description='Passionate software developer!')
        self.speaker.save()

    def test_create(self):
        """ Speaker instance should be saved. """
        self.assertEquals(1, self.speaker.pk)

    def test_unicode(self):
        """ Speaker string representation should be the name. """
        self.assertEquals(u'Matheus Oliveira', unicode(self.speaker))


class ContactModelTest(TestCase):

    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Matheus Oliveira',
            slug='matheus-oliveira',
            url='http://coder42.com/',
            description='Passionate software developer!')

    def test_email(self):
        """ Contact must have save kind phone """
        contact = Contact.objects.create(speaker=self.speaker, kind='P',
                                         value='21-98170-0339')
        self.assertEquals(1, contact.pk)

    def test_fax(self):
        """ Contact must save kind fax """
        contact = Contact.objects.create(speaker=self.speaker, kind='F',
                                         value='21-98170-0339')
        self.assertEquals(1, contact.pk)

    def test_kind(self):
        """ Contact kind should be limited to P, F or E """
        contact = Contact(speaker=self.speaker, kind='A',
                          value='21-98170-0339')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_unicode(self):
        """ Contact string representation should be unicode. """
        contact = Contact(speaker=self.speaker, kind='E',
                          value='oliveira.matheusde@gmail.com')
        self.assertEquals(u'oliveira.matheusde@gmail.com', unicode(contact))
