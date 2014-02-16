# coding: utf-8
from django.test import TestCase
from django.db import IntegrityError
from datetime import datetime
from subscriptions.models import Subscription


class SubscriptionTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Matheus',
            cpf='36462297808',
            email='oliveira.matheusde@gmail.com',
            phone='(16) 981700339')

    def test_create(self):
        """ Subscription must have name, cpf, email and phone. """
        self.obj.save()
        self.assertEquals(1, self.obj.pk)

    def test_has_created_at(self):
        """ Subscription must have automatic created_at. """
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_unicode(self):
        self.assertEquals(u'Matheus', unicode(self.obj))


class SubscriptionUniqueTest(TestCase):
    def setUp(self):
        # Create a first entry to force colision.
        Subscription.objects.create(
            name='Matheus',
            cpf='36462297808',
            email='oliveira.matheusde@gmail.com',
            phone='(16) 981700339')

    def test_cpf_unique(self):
        """ CPF must be a unique. """
        s = Subscription(
            name='Matheus',
            cpf='36462297808',
            email='matheus@gmail.com',
            phone='(16) 981700339')
        self.assertRaises(IntegrityError, s.save)

    def test_email_unique(self):
        """ CPF must be a unique. """
        s = Subscription(
            name='Matheus',
            cpf='36462297810',
            email='oliveira.matheusde@gmail.com',
            phone='(16) 981700339')
        self.assertRaises(IntegrityError, s.save)
