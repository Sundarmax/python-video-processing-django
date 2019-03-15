from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(blank=True)
    pic = models.FileField(upload_to='pics', blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

class FileUpload(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    datafile = models.FileField()