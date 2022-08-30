from distutils.command.upload import upload
from statistics import mode
from turtle import title
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS = (
    (0,"Draft"),
    (1,"publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(upload_to='featured_image/%Y/%m/%d')
    
    class Meta:
        ordering = ['-created_on']
        
    def __str__(self):
        return self.title
    

class Galary(models.Model):
    title = models.ImageField(upload_to='images')
    jpeg = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.title
