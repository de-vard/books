from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):
    image = models.ImageField("Изображение", upload_to='user_image/%Y/%m/%d', blank=True)
