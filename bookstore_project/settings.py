"""
Django settings for bookstore_project project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os.path
from pathlib import Path
import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)  # читаем файлы в переменной среде

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/


SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG')

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',  # встроенная подсистема разграничения доступа. Используется административным сайтом
    'django.contrib.contenttypes',  # хранит список всех моделей, объявленных во всех приложениях сайта.
    'django.contrib.sessions',  # обрабатывает серверные сессии
    'django.contrib.messages',  # выводит всплывающие сообщения
    'django.contrib.staticfiles',  # обрабатывает статические файлы

    # для allauth и для создание статических станиц в админке
    'django.contrib.sites',
    'django.contrib.flatpages',

    # allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.vk',

    # Third-party для подключения стилей к форме
    'crispy_forms',

    # каптча
    'captcha',

    # ckeditor текстовый редактор для админки
    'ckeditor',
    'ckeditor_uploader',

    # django-debug-toolbar
    'debug_toolbar',

    # django-spurl для пагинации (использовал в контроллере фильтров)
    'spurl',

    # local
    'users.apps.UsersConfig',
    'pages.apps.PagesConfig',
    'books.apps.BooksConfig',
    'orders.apps.OrdersConfig',  # TODO: приложение оплаты не доделано
]

MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',  # кеширование
    'django.middleware.security.SecurityMiddleware',  # реализует дополнительную защиту сайта от сетевых атак
    'django.contrib.sessions.middleware.SessionMiddleware',  # обрабатывает Серверные сессии на низком уровне
    'django.middleware.common.CommonMiddleware',  # участвует в предварительной обработке запросов
    'django.middleware.csrf.CsrfViewMiddleware',
    # осуществляет защиту ОТ межсайтовых атак при обработке данных, переданных сайту HTTP-методом POST
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # добавляет В объект запроса атрибут, хранящий текущего пользователя. Через этот атрибут в контроллерах и
    # шаблонах можно выяснить, какой пользователь выполнил вхо
    'django.contrib.messages.middleware.MessageMiddleware',  # обрабатывает ВСПЛЫВающие сообщения на низком уровне.
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # реализует дополнительную защиту сайта от сетевых атак.
    'debug_toolbar.middleware.DebugToolbarMiddleware',  # debug-toolbar
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',  # создание статических станиц в админке
    'django.middleware.cache.FetchFromCacheMiddleware',  # кеширование
]

ROOT_URLCONF = 'bookstore_project.urls'  # путь к модулю, в котором записаны маршруты уровня проекта в виде строки

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bookstore_project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': env('ENGINE'),
        'NAME': env('NAME'),
        'USER': env('USER'),
        'PASSWORD': env('PASSWORD'),
        'HOST': env('HOST'),
        'PORT': env('PORT'),
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]  # путь где находится папка
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]  # мы указываем в каком порядке искать статические файлы

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # абсолютный путь файловой системы к каталогу для загруженных
# пользователем файлов


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'users.CustomUser'  # Указываем на модель нового пользователя
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# allauth config
LOGIN_REDIRECT_URL = 'home'  # перенаправление после входа пользователя на сайт
ACCOUNT_LOGOUT_REDIRECT = 'home'  # перенаправление после выхода пользователя на сайт
SITE_ID = 1
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = 'none'

# smtp для отправки на почту писем
RECIPIENTS_EMAIL = [env('EMAIL_1')]  # список почт получателей по уполчанию
DEFAULT_FROM_EMAIL = env('EMAIL_1')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = env('EMAIL_2')  # от какого эмаила будет почта
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# ckeditor
CKEDITOR_UPLOAD_PATH = "uploads/"  # настройка пути куда будут загружены изображения (настройка для ckeditor)

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        # 'skin': 'office2013',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms',
             'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                       'HiddenField']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['About']},
            '/',  # put this to force next toolbar on new line
            {'name': 'yourcustomtools', 'items': [
                # put the name of your editor.ui.addButton here
                'Preview',
                'Maximize',
                'Youtube',

            ]},
        ],
        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
        # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        # 'height': 291,
        # 'width': '100%',
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage',  # the upload image feature
            # your extra plugins here
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            # 'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath',
            'youtube',
        ]),
    }
}

# debug-toolbar
INTERNAL_IPS = [
    "127.0.0.1",
]
OPTIONS: {
    'timeout': 300,
}

# кеширование
CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 600  # 604800  # время хранения кеша
CACHE_MIDDLEWARE_KEY_PREFIX = ''