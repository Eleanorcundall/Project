from django.shortcuts import render
from django.http import HttpResponse

def home_feed_view(request):
    return HttpResponse("Testing ItGirl Blog")
