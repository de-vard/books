from django.urls import path
from .views import BookListView, BookDetailView, SearchResultsView, FilterBookView

vals = {'pk': 1}  # переменная для сортировки по умолчанию

urlpatterns = [
    path('', BookListView.as_view(), vals, name='book_list'),
    path('sort/<int:pk>/', BookListView.as_view(), name='sort'),
    path('filter/', FilterBookView.as_view(), vals, name='filter'),
    path('<uuid:pk>', BookDetailView.as_view(), name='book_detail'),
    path('search/', SearchResultsView.as_view(), name='search_results'),

]
