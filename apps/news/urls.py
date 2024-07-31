from django.urls import path 

from .views import *

urlpatterns = [
    path('', NewsAPIView.as_view(), name='api_news '),
    path('create/', NewsAPICreate.as_view(), name='api_news_create '),
    path('<int:pk>/', NewsAPIRetrieve.as_view(), name='api_news_retrieve '),
    path('update/<int:pk>/', NewsAPIUpdate.as_view(), name='api_news_update '),
    path('delete/<int:pk>/', NewsAPIDestroy.as_view(), name='api_news_delete '),




]