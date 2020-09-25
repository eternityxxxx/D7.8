from django.urls import path
from .views import BookListPage, user_account, BookPage


app_name = 'p_library'

urlpatterns = [
   path('', BookListPage.as_view(), name='books_list'),
   path('book/<str:pk>', BookPage.as_view(), name='book'),
   path('account/', user_account, name='account'),
]
