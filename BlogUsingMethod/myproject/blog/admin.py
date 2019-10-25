from django.contrib import admin
from .models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','image_tag','content','updated','timestamp']

admin.site.register(Post,PostAdmin)