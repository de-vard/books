"""bookstore_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static

urlpatterns = [
    # django admin
    path('admin/', admin.site.urls),

    # user management allauth
    path('accounts/', include('allauth.urls')),

    # ckeditor
    path('ckeditor/', include('ckeditor_uploader.urls')),

    # капча
    path('captcha/', include('captcha.urls')),

    # flatpages для создания статических страниц через админку
    path('pages/', include('django.contrib.flatpages.urls')),

    path('i18n/', include('django.conf.urls.i18n')),

    # Local apps
    path('', include('pages.urls')),
    path('user', include('users.urls')),
    path('books/', include('books.urls')),
    path('orders/', include('orders.urls')),
]

if settings.DEBUG:
    from .settings import DEBUG
    # 'debug_toolbar
    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
