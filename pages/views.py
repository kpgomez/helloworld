# from django.shortcuts import render (default)
from django.http import HttpResponse

# Create your views here. (default)
def homePageView(request):
    return HttpResponse("Hello, World!")
