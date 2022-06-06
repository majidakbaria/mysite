from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse,JsonResponse



def home_view(request):
    return render(request, 'application/home.html')       #In this code we return a html code


def contact_view(request):
    return render(request, 'application/contact.html')      #In this code we return the json code



def index_view(request):
    return render(request, 'application/index.html')