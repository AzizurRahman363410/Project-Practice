from django.db import models
from django.utils.html import format_html
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    image =  models.ImageField(upload_to='picture/')
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title
# showing image
    def image_tag(self):
        return format_html('<img src="/media/%s" width="100"/>'%self.image)
    #changing image field name
    image_tag.short_description = 'Image'

