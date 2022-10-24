from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model

class UserListView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    context_object_name = 'my_user'
    template_name = 'user/user_detail.html'
    login_url = 'account_login'  # куда перенаправлять пользователей, если они не зарегестрированны

