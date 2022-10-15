#!-*-coding:utf-8-*-
import json

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from recipes.models import Ingredient, Tag, Recipe
from users.models import User


class ReciepeViewTestCase(TestCase):
    """Тест api рецептов."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.url = reverse('api:recipes-list')

        cls.guest_client = Client()
        cls.user = User.objects.create_user(
            username='admin',
            password='admin',
            first_name='egor',
            last_name='letov',
        )
        cls.auth_client = Client()

    def setUp(self) -> None:
        self.auth_client.force_login(user=self.user)

        self.ing_salt = Ingredient.objects.create(
            name='salt',
            measurement_unit='g'
        )
        self.tag1 = Tag.objects.create(
            name='tag1',
            color='red',
            slug='tag1',
        )
        self.tag2 = Tag.objects.create(
            name='tag2',
            color='blue',
            slug='tag2',
        )

    def test_create_recipe(self):
        """Тест создания рецепта.

        Как домашнее задание, добавить авторизацию по токену.
        """
        data = {
            "ingredients": [
                {
                    "id": self.ing_salt.id,
                    "amount": 10,
                },
            ],
            "tags": [self.tag1.pk, self.tag2.pk],
            "name": "pay",
            "text": "cook pay",
            "cooking_time": 1,
        }
        client = APIClient()
        client.force_login(user=self.user)

        resp = self.auth_client.post(path=self.url, data=json.dumps(data),
                                     content_type='application/json')

        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(resp.data.get('id'), Recipe.objects.last().id)
