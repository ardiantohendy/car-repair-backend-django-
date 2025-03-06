from rest_framework.response import Response
from rest_framework.decorators import api_view
from book.models import Book
from .serializer import BookSerializer 


@api_view(['GET'])
def getData(request):
    book = Book.objects.all()
    serializer = BookSerializer(book, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addBook(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)