from django.test import TestCase
from django.urls import reverse

from .models import Cake, Salad


class CakeModelTest(TestCase):
    def setUp(self):
        Cake.objects.create(title='Cake', price='Cake Price',
                            description='Cake Description')

    def test_title_content(self):
        cake = Cake.objects.get(id=1)
        expected_object_name = f"{cake.title}"
        self.assertEqual(expected_object_name, 'Cake')

    def test_price_content(self):
        cake = Cake.objects.get(id=1)
        expected_object_name = f"{cake.price}"
        self.assertEqual(expected_object_name, 'Cake Price')

    def test_description_content(self):
        cake = Cake.objects.get(id=1)
        expected_object_name = f"{cake.description}"
        self.assertEqual(expected_object_name, 'Cake Description')

    def test_page_status_code(self):
        response = self.client.get('/menu/cake/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('cake'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('cake'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu.html')


class SaladModelTest(TestCase):
    def setUp(self):
        Salad.objects.create(title='Salad', price='Salad Price',
                             description='Salad Description')

    def test_title_content(self):
        salad = Salad.objects.get(id=1)
        expected_object_name = f"{salad.title}"
        self.assertEqual(expected_object_name, 'Salad')

    def test_price_content(self):
        salad = Salad.objects.get(id=1)
        expected_object_name = f"{salad.price}"
        self.assertEqual(expected_object_name, 'Salad Price')

    def test_description_content(self):
        salad = Salad.objects.get(id=1)
        expected_object_name = f"{salad.description}"
        self.assertEqual(expected_object_name, 'Salad Description')

    def test_page_status_code(self):
        response = self.client.get('/menu/salad/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('salad'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('salad'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu.html')
