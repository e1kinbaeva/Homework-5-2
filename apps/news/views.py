from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView,RetrieveAPIView, UpdateAPIView,DestroyAPIView

from .models import News
from .serializers import *
# Create your views here.

class NewsAPIView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class NewsAPICreate(CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsCreateSerializer

class NewsAPIRetrieve(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsCreateSerializer

class NewsAPIUpdate(UpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsCreateSerializer

class NewsAPIDestroy(DestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsCreateSerializer