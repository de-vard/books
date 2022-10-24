from django.urls import path
from .views import HomePageView, ContactFormView


urlpatterns = [
    path('featback/', ContactFormView.as_view(), name='featback'),
    path('', HomePageView.as_view(), name='home'),
]
