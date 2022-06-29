from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse,JsonResponse



def index_view(request):
    return render(request, 'application/index.html')       #In this code we return a html code


def about_view(request):
    return render(request, 'application/about.html')      #In this code we return the json code



def contact_view(request):
    return render(request, 'application/contact.html')