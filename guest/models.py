from django.db import models
from Admin.models import *

# Create your models here.


class User(models.Model):
    user_name=models.CharField(max_length=50)
    user_contact=models.CharField(max_length=50)
    user_email=models.EmailField(unique=True)
    user_gender=models.CharField(max_length=50)
    user_address=models.TextField(null=True)
    user_zipcode=models.CharField(max_length=50)
    user_photo=models.FileField(upload_to='userdocs/')
    user_proof=models.FileField(upload_to='userdocs/')
    user_pwd=models.CharField(max_length=50,unique=True)
    user_doj=models.DateField(auto_now=True)
    user_vsts=models.IntegerField(default=0)
    user_place=models.ForeignKey(Place,on_delete=models.SET_NULL,null=True)
    
class Owner(models.Model):
    owner_name=models.CharField(max_length=50)
    owner_contact=models.CharField(max_length=50)
    owner_email=models.EmailField(unique=True)
    owner_gender=models.CharField(max_length=50)
    owner_address=models.TextField(null=True)
    owner_zipcode=models.CharField(max_length=50)
    owner_photo=models.FileField(upload_to='ownerdocs/')
    owner_proof=models.FileField(upload_to='ownerdocs/')
    owner_pwd=models.CharField(max_length=50,unique=True)
    owner_doj=models.DateField(auto_now=True)
    owner_vsts=models.IntegerField(default=0)
    owner_place=models.ForeignKey(Place,on_delete=models.SET_NULL,null=True)
    
    
