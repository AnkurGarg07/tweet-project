from django.shortcuts import render,redirect


def home(request):
    return redirect('tweet_list')