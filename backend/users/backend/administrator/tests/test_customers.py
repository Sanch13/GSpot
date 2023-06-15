import datetime

from django.contrib.auth.models import AbstractUser
from django.urls import reverse

from administrator.models import Admin
from base.base_tests.tests import BaseTestView
from django.test import TestCase
from common.models import Country
from customer.models import CustomerUser


class CustomersViewTest(BaseTestView, TestCase):
    url = reverse('admin_customers')
    user: AbstractUser
    admin: Admin

    @classmethod
    def setUpTestData(cls):
        Country.objects.create(id=1, name='Russia')
        cls.admin = Admin.objects.create_superuser(
            'admin3', 'admin2@admin.com', 'admin', '9803515667'
        )
        cls.user = CustomerUser.objects.create_user(
            username="test_user",
            email="email@mail.ru",
            password="test_user1",
            first_name="user_test_name",
            last_name="user_test_name",
            phone="89991234567",
            birthday=datetime.date.today(),
        )

    def test_000_list_customer(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.admin))
        request = self.client.get(self.url)
        self.assertEqual(request.status_code, 200)

    def test_01_block_customer(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.admin))
        payload = {'reason': 'Test reason'}
        request = self.client.post(f"{self.url}{self.user.id}/block", payload, format='json')
        self.assertEqual(request.status_code, 201)

    def test_02_unblock_customer(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.admin))
        request = self.client.post(f"{self.url}{self.user.id}/unblock")
        self.assertEqual(request.status_code, 200)

    def test_03_delete(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.admin))
        request = self.client.delete(f'{self.url}{self.user.id}/')
        self.assertEqual(request.status_code, 204)
