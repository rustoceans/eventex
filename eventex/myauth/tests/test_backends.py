# coding: utf-8
from unittest import skip
from django.test import TestCase
from django.test.utils import override_settings
from django.contrib.auth import get_user_model
from eventex.myauth.backends import EmailBackend


@skip
class EmailBackendTest(TestCase):

    def setUp(self):
        UserModel = get_user_model()
        UserModel.objects.create_user(username='matheus',
                                      email='oliveira.matheusde@gmail.com',
                                      password='123')
        self.backend = EmailBackend()

    def test_authenticate_with_email(self):
        user = self.backend.authenticate(email='oliveira.matheusde@gmail.com',
                                         password='123')

        self.assertIsNotNone(user)

    def test_wrong_password(self):
        user = self.backend.authenticate(email='oliveira.matheusde@gmail.com',
                                         password='wrong')

        self.assertIsNone(user)

    def test_unkown_user(self):
        user = self.backend.authenticate(email='unkown@gmail.com',
                                         password='123')

        self.assertIsNone(user)

    def test_get_user(self):
        self.assertIsNotNone(self.backend.get_user(1))


@skip
class MultipleEmailTeste(TestCase):
    def setUp(self):
        UserModel = get_user_model()
        UserModel.objects.create_user(username='matheus',
                                      email='oliveira.matheusde@gmail.com',
                                      password='123')
        UserModel.objects.create_user(username='matheus2',
                                      email='oliveira.matheusde@gmail.com',
                                      password='123')
        self.backend = EmailBackend()

    def test_multiple_emails(self):
        user = self.backend.authenticate(email='oliveira.matheusde@gmail.com',
                                         password='123')

        self.assertIsNone(user)


@skip
@override_settings(AUTHENTICATION_BACKENDS=(
    'eventex.myauth.backends.EmailBackend',))
class FunctionalEmailBackendTest(TestCase):

    def setUp(self):
        UserModel = get_user_model()
        UserModel.objects.create_user(username='matheus',
                                      email='oliveira.matheusde@gmail.com',
                                      password='123')
        self.backend = EmailBackend()

    def test_login_with_email(self):
        result = self.client.login(email='oliveira.matheusde@gmail.com',
                                   password='123')

        self.assertTrue(result)

    def test_login_with_username(self):
        result = self.client.login(username='oliveira.matheusde@gmail.com',
                                   password='123')

        self.assertTrue(result)
