from django.db import models
# Create your models here.

class Contact(models.Model):
    name=models.CharField(null=False,max_length=100)
    email=models.EmailField(null=False,max_length=254)
    phone=models.CharField(default="",blank=False,max_length=10)
    msg=models.CharField(default="",max_length=1000)

    def __str__(self):
        return self.name