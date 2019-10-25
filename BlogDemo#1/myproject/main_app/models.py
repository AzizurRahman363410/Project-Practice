from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    date_timeField = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('main_app.Category', blank=True, null=True, on_delete=models.CASCADE )
    discription = models.TextField(default='')
    image = models.ImageField()

    def __str__(self):
        return self.title


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    def __str__(self):
        return self.category_name