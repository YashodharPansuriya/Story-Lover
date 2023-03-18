
from django.contrib import admin
from django.urls import path
from book_api.views import BookList, BookCreate


urlpatterns = [
    path('', BookCreate.as_view()),
    path('list/', BookList.as_view()),
    
]
