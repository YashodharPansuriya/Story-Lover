from django.shortcuts import render
from book_api.models import Book # this is class
from django.http import JsonResponse

# Create your views here.
def book_list(request):
    books = Book.objects.all() # it return the object 
    books_Python = list(books.values()) # it return list
    return JsonResponse({    #convert list into the json format 
        'book' : books_Python    # dictionary
    })