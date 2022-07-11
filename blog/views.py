from django.shortcuts import render,get_object_or_404
from application.models import post

# Create your views here.

def blog_index_view(request):
    posts=post.objects.filter(status=1)
    context={'posts':posts}
    return render (request, 'blog/blog-home.html',context)

def blog_single_view(request,pid):
    p = get_object_or_404(post,pk=pid,status=1)   #dar inja agar hamchin posti vojood nadashte bashe error 404 mide.
    context={'post':p}
    return render (request, 'blog/blog-single.html',context)

def test_view(request,pid):
    #p = post.objects.get(id=pid)        #dar inja agar hamchin posti vojood nadashte bashe error doesnt exist mide.
    posts= post.objects.filter(status=1)
    p = get_object_or_404(posts,pk=pid)   #dar inja agar hamchin posti vojood nadashte bashe error 404 mide.
    context={'post':p}
    #context={'name':name,'lastname':lastname,'gender':gender}
    return render (request, 'test.html',context)


