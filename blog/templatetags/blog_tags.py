from django import template
from application.models import post

register = template.Library()

@register.simple_tag()   #tabe ra bayad be onvane simple_tag register konim.
def postcounter(): 
    posts=post.objects.all().count()
    return posts


@register.simple_tag()   
def posts(): 
    p=post.objects.all()
    return p

    

    