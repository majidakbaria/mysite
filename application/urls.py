from django.contrib import admin
from django.urls import path
from application.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', home_view),
    path("contact", contact_view),
    path("index",index_view)
]