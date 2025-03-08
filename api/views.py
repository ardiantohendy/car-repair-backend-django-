from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from book.models import Book
from .serializer import BookSerializer, UserSerializer


# USER AUTHENTICATION USING JWT

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


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