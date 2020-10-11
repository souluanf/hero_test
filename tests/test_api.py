from apps.authh.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase


class TestApiDrf(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.password = '2056'
        cls.user = User.objects.create_user(
            'testeapi@testeapi.com',
            cls.password,
        )
        cls.client = APIClient()
        url = reverse('token_obtain_pair')
        data = {
            'email': cls.user.email,
            'password': cls.password
        }
        response = cls.client.post(url, data=data)
        cls.tokens = response.data

    # ---------TESTS----------#
    def test_create_company(self):
        url = reverse('api-root:empresas-list')
        data = {
            "name": "Company Hero",
            "cnpj": "11122233344",
            "uf": "SP"
        }

        auth = 'Bearer {0}'.format(self.tokens['access'])
        response = self.client.post(url, data, HTTP_AUTHORIZATION=auth)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # def test_create_employee(self):
    #     url = reverse('api-root:funcionarios-list')
    #     data = {
    #         "full_name": "luan Fernandest",
    #         "email": "company@hero.com",
    #         "companies": [1]
    #     }
    #
    #     auth = 'Bearer {0}'.format(self.tokens['access'])
    #     response = self.client.post(url, data, HTTP_AUTHORIZATION=auth)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_list_empresas(self):
        url = reverse('api-root:empresas-list')
        auth = 'Bearer {0}'.format(self.tokens['access'])
        response = self.client.get(url, HTTP_AUTHORIZATION=auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_list_funcionarios(self):
        url = reverse('api-root:funcionarios-list')
        auth = 'Bearer {0}'.format(self.tokens['access'])
        response = self.client.get(url, HTTP_AUTHORIZATION=auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_list_user_by_username(self):
        url = reverse('search-employee', args=['testeapi@testeapi.com'])
        auth = 'Bearer {0}'.format(self.tokens['access'])
        response = self.client.get(url, HTTP_AUTHORIZATION=auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_list_companies_by_name(self):
        url = reverse('search-company', args=['Company Hero'])
        auth = 'Bearer {0}'.format(self.tokens['access'])
        response = self.client.get(url, HTTP_AUTHORIZATION=auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK)