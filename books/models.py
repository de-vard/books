import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Author(models.Model):
    """Класс авторов"""
    name = models.CharField('Имя автора', max_length=200)
    cover = models.ImageField("Изображение", upload_to='covers/%Y/%m/%d', blank=True)
    description = models.TextField('Oписание атора', blank=True)

    CHOICE = (
        ('a', ' Автор просто суппер'),
        ('b', 'Автор средний'),
        ('c', 'Автор ужастный'),
    )
    choice = models.CharField(max_length=1, choices=CHOICE,)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Category(models.Model):
    """Категории"""
    name = models.CharField("Категория", max_length=150)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'



class Book(models.Model):
    """Класс книги"""
    id = models.UUIDField("ID-UUID", primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Название", max_length=200)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET('Вы удалили категорию'),# SET—Заносит В ПОЛе внешнего ключа указанное значение:
        verbose_name='Категория',
        db_index=True,
        null="Без_категории",
        blank=True
    )
    CHOICE = (
        ('a', 'ru'),
        ('b', 'en'),
        ('c', 'other'),
    )
    language = models.CharField(max_length=1, choices=CHOICE,  verbose_name="Язык", db_index=True,)
    description = models.TextField('Текст описания', blank=True)
    files = models.FileField(upload_to='book/%Y/%m/%d', blank=True, verbose_name='Файлы книг')
    author = models.ForeignKey(
        Author,
        on_delete=models.DO_NOTHING, # НЕ чего не делать при удалении первичного класса
        verbose_name='Автор'
    )
    price = models.DecimalField('Ценна', max_digits=6, decimal_places=2)
    cover = models.ImageField("Изображение", upload_to='covers/%Y/%m/%d', blank=True)
    come_out = models.IntegerField('Год выхода', blank=True, null=1932)
    edition = models.CharField("Издание", max_length=200, blank=True)
    draft = models.BooleanField('Черновик', default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])

    def get_review(self):
        return self.reviews.filter(parent__isnull=True)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

        indexes = [
            models.Index(fields=['id'], name='id_index'),  # Индексация
        ]

        permissions = [
            ('special_status', 'Can read all books'),  # разрешение для пользователя что он может читать книгу
        ]


class Review(models.Model):
    """Класс коментариев"""
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='reviews' # related_name — (По простому ты сможешь из первичного класса обращатся к вторичному ) имя атрибута записи первичной модели, предназначенного для доступа к связанным записям вторичной модели, в виде строки
    )
    review = models.CharField( max_length=255)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Автор')
    date_posted = models.DateTimeField(auto_now_add=True, blank=True, null=2008)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')  #

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
        ordering = ['-date_posted']  # cортируем (эта сортировка применяется везде)


    def __str__(self):
        return self.review
