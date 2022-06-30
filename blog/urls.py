from django.contrib import admin
from django.urls import path
from application.views import *
from blog.views import *

app_name = "blog"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_view, name="index"),
    path('/single', blog2_view, name='single')
]