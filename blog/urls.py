from django.contrib import admin
from django.urls import path
from application.views import *
from blog.views import *

app_name = "blog"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_index_view, name="index"),
    path('<int:pid>', blog_single_view, name='single'),
    #path('<str:name>/<str:lastname>/gender/<str:gender>', test_view, name='test') #url haye ma mitoone ham static bashe ham dynamic
    #path('post-<int:pid>', test_view, name='test')
    path('test',test_view,name='test')

]