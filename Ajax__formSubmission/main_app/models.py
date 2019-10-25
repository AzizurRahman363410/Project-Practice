from django.db import models

# Create your models here.

    
from django.db import models

class Post (models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title
    class Meta:
        db_table = 'Post'
        managed = True
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-id']