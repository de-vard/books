from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from .forms import ContactForm
from django.core.mail import send_mail
from bookstore_project.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL


class ContactFormView(FormView):
    """Класс для ввывода формы обратной связи"""
    form_class = ContactForm
    template_name = 'about.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        """ Проверка вилидности"""

        name = form.cleaned_data['name']  # получение данных из формы
        email = form.cleaned_data['email']  # получение данных из формы
        content = form.cleaned_data['content']  # получение данных из формы

        send_mail(
            f'Вам отправил почту:{name} c emaila:{email}',
            content,
            DEFAULT_FROM_EMAIL,
            RECIPIENTS_EMAIL
        )

        return redirect('home')


class HomePageView(TemplateView):
    template_name = 'home.html'
