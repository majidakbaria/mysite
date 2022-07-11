
from django.db import models

# Create your models here.

class post(models.Model):

    #category
    #tag
    title=models.CharField(max_length=240,default="hi")
    content=models.CharField(max_length=230,default="hello")
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



    