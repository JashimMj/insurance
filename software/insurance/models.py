from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileM(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    Phone=models.CharField(max_length=100,null=True,blank=True)
    Present_Address=models.CharField(max_length=255,null=True,blank=True)
    Permanant_Address=models.CharField(max_length=255,null=True,blank=True)
    Image=models.ImageField(upload_to='User',null=True,blank=True)
    objects=models.Manager()

    def images(self):
        try:
            urls=self.Image.url
        except:
            urls=''
        return urls

class ItemEntryM(models.Model):
    Itemname=models.CharField(max_length=255,null=True,blank=True)
    Unit=models.CharField(max_length=255,null=True,blank=True)
    objects=models.Manager()

class SupplierInfoM(models.Model):
    Suppliername=models.CharField(max_length=255,null=True,blank=True)
    Address=models.TextField(max_length=2000,null=True,blank=True)
    Phone=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    objects=models.Manager()

