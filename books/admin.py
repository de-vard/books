from django import forms
from django.contrib import admin
from .models import Book, Review, Author, Category
from django.utils.safestring import mark_safe

from ckeditor_uploader.widgets import CKEditorUploadingWidget


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Категории"""
    list_display = ('id', 'name', 'url')
    list_display_links = ('id',)  # не обходим для list_editable, так как назначает сылку для подробного перехода
    # статьи
    list_editable = ('name', 'url')  # для быстрого редактирования админки
    prepopulated_fields = {'url': (
        'name',)}  # Основное использование этой функции состоит в том, чтобы автоматически генерировать значение для
    # SlugFieldполя из одного или нескольких другие поля


class BookAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Book
        fields = '__all__'


class ReviewInline(admin.TabularInline):  # Используем класс для отображение коментарриев в модели книги
    """Отзывы"""
    model = Review
    extra = 1  # сколько пустых отзывов отображать
    readonly_fields = ('author',)  # скрываем столбци что бы их в админке не могли редактироват


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Книга"""
    inlines = [
        ReviewInline,
    ]
    form = BookAdminForm
    list_display = ('author', 'title', 'price',)
    list_display_links = ('author',)  # не обходим для list_editable, так как назначает сылку для подробного перехода
    # статьи
    list_filter = ('category', 'come_out')  # Фильтрациия по полям
    save_on_top = True  # Переносим меню в вверх
    save_as = True  # добавление книпки "сохранить как новый обьект"
    list_editable = ('title', 'price')  # для быстрого редактирования админки
    readonly_fields = ('get_image',)  # Выводим мини изображение полученное из функции
    actions = ['publish', 'unpublish']  # реализация экшинов в админостративной панели

    def get_image(self, obj):
        """Метод вывода мини изображение в админке"""
        return mark_safe(f"'<img src={obj.cover.url} width='50' height='60'>'")

    def unpublish(self, request, queryset):  # реализация экшинов в админостративной панели

        """Снять с публикации"""
        draft = queryset.update(draft=True)
        if draft == 1:
            message_bit = "1 запись была обновленна"
        else:
            message_bit = f'{draft} записей были обновлены'
        self.message_user(request, f'{message_bit}')

    def publish(self, request, queryset):  # реализация экшинов в админостративной панели
        """Oпубликации"""
        draft = queryset.update(draft=False)
        if draft == 1:
            message_bit = "1 запись была обновленна"
        else:
            message_bit = f'{draft} записей были обновлены'
        self.message_user(request, f'{message_bit}')


class AutorAdmin(admin.ModelAdmin):
    """Класс авторов"""
    list_display = ('name', 'cover', )



admin.site.register(Author, AutorAdmin)
