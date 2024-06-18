from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('tweet_list/',views.tweet_list,name='tweet_list'),
    path('tweet_create/',views.create_tweet,name='tweet_create'),
    path('tweet_delete/<int:tweet_id>/',views.tweet_delete,name='tweet_delete'),
    path('tweet_edit/<int:tweet_id>/',views.tweet_edit,name='tweet_edit'),
    path('register/',views.register,name='register'),
]
