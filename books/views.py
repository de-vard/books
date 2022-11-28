from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Book, Category
from .forms import CommentForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.urls import reverse
from django.db.models import Q


class GenreYear:
    """ Класс наследуеют классы где нужно вывести
        (выборку по категориям или другим полям модели).
        Этот класс как альтернатива методу get_context_data
     """

    def get_category(self):
        """Получение всех катерогий"""
        return Category.objects.all()

    def get_years(self):
        """ Получение все книг которые не черновики и забираем значение столбца come_out
            Для вывода только уникальных записей служит метод distinct()
        """
        return Book.objects.filter(draft=False).values("come_out").distinct()

    def get_language(self):
        """ Получение все книг которые не черновики
            и забираем только уникальные значения поля language
        """
        return Book.objects.filter(draft=False).all().distinct('language', )


class FilterBookView(GenreYear, ListView):
    """ Фильтр """
    template_name = 'books/book_list.html'
    paginate_by = 4  # пагинация

    def get_queryset(self):
        queryset = Book.objects.filter(
            Q(come_out__in=self.request.GET.getlist('come_out')) |
            Q(category__in=self.request.GET.getlist('category')) |
            Q(language__in=self.request.GET.getlist('language'))
        )  # с помощью метода GET мы будем
        # доставать все значения годов и категорий и язык из html
        return queryset


class BookListView(LoginRequiredMixin, GenreYear, ListView):
    """Класс просмотра всех книг"""

    model = Book
    paginate_by = 4  # пагинация
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'
    login_url = 'account_login'  # куда перенаправлять пользователей, если они не зарегестрированны

    def get_queryset(self):
        """ Сортировка """
        pk = self.kwargs['pk']
        if pk == 1:
            sort_name = Book.objects.order_by('price')
        elif pk == 2:
            sort_name = Book.objects.order_by('-price')
        return sort_name


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, FormMixin, DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    login_url = 'account_login'  # куда перенаправлять пользователей, если они не зарегестрированны
    permission_required = 'books.special_status'
    form_class = CommentForm

    def get_success_url(self):
        """Перенаправление при сохранении коментариев"""
        return reverse('book_detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        """Метод, который добавляем данные в шаблон"""
        context = super(BookDetailView, self).get_context_data(**kwargs)  # пишем метод get_context_data  и вызываем
        # супер нашего родителя, таким образом мы получаем словарь, после обрашаемся к context что бы добавить новые
        # элементы паременны и так далее
        context['form'] = CommentForm(initial={'reviews': self.object})
        return context

    def post(self, request, *args, **kwargs):
        """Проверка на валидность формы"""
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        """ Сохранения коментария"""
        form = form.save(commit=False)  # Приостанавливаем сохранение

        form.author = self.request.user  # Автоматически подставляем пользователя

        form.book = self.get_object()  # Получаем от get_object таблицу id модели Book и связываем коментарий с ней

        form.save()  # Сохраняем комментарий
        return super(BookDetailView, self).form_valid(form)


class SearchResultsView(ListView):
    """Класс для ввывода результат поиска"""
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'
    paginate_by = 2  # пагинация

    def get_context_data(self, **kwargs):
        """Получаем из url q и передаем ее значение в шаблон
            это для пагинации
        """
        context = super(SearchResultsView, self).get_context_data(**kwargs)  # пишем метод get_context_data  и вызываем
        # супер нашего родителя, таким образом мы получаем словарь, после обрашаемся к context что бы добавить новые
        # элементы переменных и так далее
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        """Поиск"""
        query = self.request.GET.get('q')  # Получает значение из перменной q которая находится в  URL
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__name__icontains=query)
        )
