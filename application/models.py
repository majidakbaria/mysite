from email.policy import default
from re import T
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):

    
    name=models.CharField(max_length=250,default='h')
    
    def __str__(self):
        return self.name


class post(models.Model):

    #category
    #tag
    category=models.ManyToManyField(Category)   #baraye ManyToManyField niaz nist null tarif konim.
    image=models.ImageField(upload_to='blog/',default='default.jpg')
    author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title=models.CharField(max_length=240,default="hi")
    content=models.TextField()   #TextField niazi be default nadare.
    counted_views=models.IntegerField(default=0)
    status=models.BooleanField(default=False)
    published_date=models.DateTimeField(null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['created_date'] #ba incode kollan ordering barasase created_date anjam mishe.
        #verbose_name = "pizza"       az verbose_name va verbos_name_plural zamani estefade mishavad ke bekhahim yek kalamaro avaz konim
        #verbose_name_plural = "stories" 


    #bedoone code zir object post ha ba id hayeshan namayesh dade mishavad.
    def __str__(self):
       return self.title
       # return " {} + {} + {} " .format(self.title,self.id,self.status) 

    def snippets(self):
        return self.content[:200] + '...'











class contact(models.Model):

    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_date',) #agar az tuple tak ozvi estefade mikonim hamtan tahesh  , bezarim. 

    def __str__(self):
       return self.name 






    
    
    
