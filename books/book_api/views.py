"""from django.shortcuts import render
from book_api.models import Book # this is class
# from django.http import JsonResponse # it gives the normal response
from rest_framework.decorators import api_view # decorator use for get request when we use rest framework
from rest_framework.response import Response
from rest_framework import status
from book_api.serializer import BookSerializer

# Create your views here.
# this fun is for GET means data is grab from the database and see into website.
@api_view(['GET'])
def book_list(request):
    books = Book.objects.all() # it return the object 
    serializer = BookSerializer(books , many=True)  # books data is convert into json format, many means many object convert json for that many=true
    return Response(serializer.data)
    ----> books_Python = list(books.values()) # it return list
    return JsonResponse({    #convert list into the json format 
        'book' : books_Python    # dictionary
    })

# this fun is for POST means data is grab from the user and store into database.
@api_view(['POST'])
def book_create(request):
    serializer = BookSerializer(data=request.data) # take data in json formate
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET','PUT','DELETE'])
def book(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except:
        return Response(
            {
                "error":"Book does not exist"
            }, status=status.HTTP_404_NOT_FOUND
        )
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        ---->return Response(
            {
                 'Delete' : True
            }
        )"""

from rest_framework.views import APIView 
from book_api.models import Book  
from book_api.serializer import BookSerializer


class BookList(APIView):
    def get(self, request):
        book = Book.objects.all()
        serializer = BookSerializer(book, many=True)
