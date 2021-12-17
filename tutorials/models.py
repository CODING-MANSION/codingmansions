from django.db import models

# Create your models here.
from embed_video.fields import EmbedVideoField

class Item(models.Model):
    video = EmbedVideoField()  # same like models.URLField()
    playlist =models.CharField(default="",max_length=100)
    desc=models.CharField(default="",max_length=10000)

