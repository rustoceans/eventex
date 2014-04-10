# coding: utf-8
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test.utils import override_settings


@override_settings(AUTH_USER_MODEL='myauth.User')
class FuncationCustomUserModelTest(TestCase):
    def setUp(self):
        UserModel = get_user_model()
        user = UserModel(cpf='12345678900')
        user.set_password('123')
        user.save()

    def test_login_with_cpf(self):
        self.assertTrue(self.client.login(cpf='12345678900', password='123'))
