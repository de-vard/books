from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm

CustomUser = get_user_model()  # сылаемся на модель пользователя

UserAdmin.fieldsets += ('Добаленные лично мной поля', {'fields': ('image',)}), # Добавляем поля модели в админку (которые мы создали ) для пользователей что бы их было видно
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'image' ]






admin.site.register(CustomUser, CustomUserAdmin)
