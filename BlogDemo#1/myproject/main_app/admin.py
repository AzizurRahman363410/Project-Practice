from django.contrib import admin
from .models import BlogPost,Category
# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    search_fields = ['title','category']
    list_filter = ['title','category']
    list_display = ['title','category','date_timeField']

admin.site.register(BlogPost,BlogPostAdmin)
admin.site.register(Category)