# coding: utf-8
from django.test import TestCase
from django.db import IntegrityError
from datetime import datetime
from eventex.subscriptions.models import Subscription


class SubscriptionTest(TestCase):
    def setUp(self):
        self.obj = Subscription(name='Matheus Oliveira', cpf='36462297808',
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
        self.assertEquals(u'Matheus Oliveira', unicode(self.obj))

    def test_paid_default_is_false(self):
        """ By default paid must be False """
        self.assertEquals(False, self.obj.paid)


class SubscriptionUniqueTest(TestCase):
    def setUp(self):
        # Create a first entry to force colision.
        Subscription.objects.create(name='Matheus Oliveira', cpf='36462297809',
                                    email='oliveira.matheusde@gmail.com',
                                    phone='(16) 981700339')

    def test_cpf_unique(self):
        """ CPF must be a unique. """
        s = Subscription(name='Matheus Oliveira', cpf='36462297809',
                         email='matheus@gmail.com',
                         phone='(16)981700339')

        self.assertRaises(IntegrityError, s.save)

    def test_email_can_repeat(self):
        """ E-mail is not unique anymore. """
        s = Subscription.objects.create(name='Matheus Oliveira',
                                        cpf='36462297810',
                                        email='oliveira.matheusde@gmail.com',
                                        phone='(16) 981700339')

        self.assertEqual(2, s.pk)
