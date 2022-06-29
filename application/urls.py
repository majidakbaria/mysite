from django.contrib import admin
from django.urls import path
from application.views import *

app_name = "application"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view , name='index'),
    path("contact", contact_view , name='contact'),
    path("about", about_view , name='about')
]