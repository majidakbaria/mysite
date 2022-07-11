from unicodedata import category
from django.contrib import admin
from  application.models import Category, post, contact
 

# Register your models here.



@admin.register(post)
class postadmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title','counted_views','author','status','published_date','created_date','updated_date' )
    list_filter = ('status','author')
    #ordering = ['title'] orderin ro az inja barmidaram va generalize mikonam to khode model.
    search_fields = ['title','content'] #ghabeliate search dar title va content ro darim.

#admin.site.register(post,postadmin) ham mishe az in code estefade kard ham az decorator


@admin.register(contact)
class contactadmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name','email','subject','created_date','updated_date' )
    #list_filter = ('status',)
    search_fields = ['name','subject']


admin.site.register(Category)




