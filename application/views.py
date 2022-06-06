from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse,JsonResponse



def home_view(request):
    return HttpResponse("<h1>Home page<h1>")       #In this code we return a html code


def contact_view(request):
    return HttpResponse('<h1>Contact page<h1>')      #In this code we return the json code



def index_view(request):
    return HttpResponse("<h1>Index page<h1>")