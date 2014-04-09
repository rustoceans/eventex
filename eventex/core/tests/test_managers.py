# coding: utf-8
from django.test import TestCase
from eventex.core.models import Contact, Speaker, Talk


class ContactCustomManagerTest(TestCase):

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


class PeriodManagerTest(TestCase):

    def setUp(self):
        Talk.objects.create(title='Morning Talk', start_time='10:00')
        Talk.objects.create(title='Afternoon Talk', start_time='12:00')

    def test_at_morning(self):
        """ Should be return only talks before 12:00. """
        self.assertQuerysetEqual(
            Talk.objects.at_morning(), ['Morning Talk'],
            lambda t: t.title)

    def test_at_afternoon(self):
        """ Should be return only talks after 12:00. """
        self.assertQuerysetEqual(
            Talk.objects.at_afternoon(), ['Afternoon Talk'],
            lambda t: t.title)
