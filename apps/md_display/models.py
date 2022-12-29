from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, null =True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE)
    description = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='research/images/', null=True, blank=True)
    def __str__(self):
        return self.title
    

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name