# coding: utf-8
from django.test import TestCase
from django.core.exceptions import ValidationError
from core.models import Speaker, Contact


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
        """ Contact must save kind phone """
        contact = Contact.objects.create(speaker=self.speaker, kind='F',
                                         value='21-98170-0339')
        self.assertEquals(1, contact.pk)

    def test_kid(self):
        """ Contact kind should be limited to P, F or E """
        contact = Contact(speaker=self.speaker, kind='A',
                          value='21-98170-0339')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_unicode(self):
        """ Contact string representation should be unicode. """
        contact = Contact(speaker=self.speaker, kind='E',
                          value='oliveira.matheusde@gmail.com')
        self.assertEquals(u'oliveira.matheusde@gmail.com', unicode(contact))


class ContactCustomManageTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(name='Matheus Oliveira',
                                   slug='matheus-oliveira',
                                   url='http://coder42.com/',
                                   description='Passionate software developer!')
        s.contact_set.add(
            Contact(kind='E', value='oliveira.matheusde@gmail.com'),
            Contact(kind='P', value='21-98170-0339'),
            Contact(kind='F', value='21-98170-0339'))

    def test_emails(self):
        """ Contact should be return every contacts emails """
        qs = Contact.emails.all()
        expected = ['<Contact: oliveira.matheusde@gmail.com>']
        self.assertQuerysetEqual(qs, expected)

    def test_phones(self):
        """ Contact should be return every contacts phones """
        qs = Contact.phones.all()
        expected = ['<Contact: 21-98170-0339>']
        self.assertQuerysetEqual(qs, expected)

    def test_fax(self):
        """ Contact should be return every contacts fax """
        qs = Contact.fax.all()
        expected = ['<Contact: 21-98170-0339>']
        self.assertQuerysetEqual(qs, expected)
