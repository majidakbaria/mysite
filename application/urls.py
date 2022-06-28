from django.contrib import admin
from django.urls import path
from application.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view),
    path("contact", contact_view),
    path("about", about_view)
]