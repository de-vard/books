from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView, AboutPageView


class HomepageTests(SimpleTestCase):

    def setUp(self):
        """ создаем переменную response что бы сылаться на нее в наших тестах"""
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        """ проверка пути '/' """
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_url_name(self):
        """ проверка name в url """
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        """Проверка использует ли страница правильный шаблон"""

        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_urls_resolves_homepageview(self):
        """ Проверяем что по пути '/' во view выполняется
            именно та функция/класс
        """
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)

    def test_homepage_does_not_contain_incorrect_html(self):
        """ Тестирует саму html страницу """
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')


class AboutPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, 'about.html')

    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.response, 'About Page')

    def test_aboutpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "Hi there! i should not be on the page.")

    def test_aboutpage_url_resolves_aboutpageiew(self):
        view = resolve('/about/')
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)
