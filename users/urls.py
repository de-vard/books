from django.urls import path
from .views import UserListView

urlpatterns = [
    path('<int:pk>/', UserListView.as_view(), name='user'),
]