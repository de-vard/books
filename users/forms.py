from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


# get_user_model мы импортировали свою модель пользователя
# через get_user_model что бы сделать одну единственную ссылку
# а не ссылаться на нее во всем нашем проекте

class CustomUserCreationForm(UserCreationForm):
    """ расширяем базовые пользовательские формы UserCreationForm """

    class Meta(UserCreationForm):
        model = get_user_model()
        fields = ('email', 'username', 'image' )  # поле password уже включен по умолчанию. Другие поля встроенные по
        # умолчанию https://docs.djangoproject.com/en/2.2/ref/contrib/auth/


class CustomUserChangeForm(UserChangeForm):
    """ расширяем базовые пользовательские формы UserChangeForm"""

    class Meta(UserChangeForm):
        model = get_user_model()
        fields = ('email', 'username', )  # поле password уже включен по умолчанию
