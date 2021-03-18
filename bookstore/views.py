from django.shortcuts import render
from .serializers import BookSerializer,Authorserializer
from .models import Author,Book
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework import viewsets,filters
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.response import Response


class bookListView(ListAPIView):
    search_fields = ['author','book']
    filter_backends = (filters.SearchFilter,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class bookCreateView(CreateAPIView):
    serializer_class = BookSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]
    



class bookRetriveView(RetrieveAPIView):
    search_fields = ['author','book']
    filter_backends = (filters.SearchFilter,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [BasicAuthentication]
    premission_classes = [IsAdminUser]

class bookUpdateView(UpdateAPIView):
    search_fields = ['author','book']
    filter_backends = (filters.SearchFilter,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]


class bookDeleteView(DestroyAPIView):
    search_fields = ['author','book']
    filter_backends = (filters.SearchFilter,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]


class authorCreateView(CreateAPIView):
    serializer_class = Authorserializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]

class authordetailsview(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = Authorserializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]
