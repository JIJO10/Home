from django.db import models
from Admin.models import *


# Create your models here.



class Officer(models.Model):
    officer_name=models.CharField(max_length=50)
    officer_contact=models.CharField(max_length=50)
    officer_email=models.EmailField(unique=True)
    officer_gender=models.CharField(max_length=50)
    officer_address=models.TextField(null=True)
    officer_photo=models.FileField(upload_to='officerdocs/')
    officer_proof=models.FileField(upload_to='officerdocs/')
    officer_pwd=models.CharField(max_length=50,unique=True)
    officer_doj=models.DateField(auto_now=True)
    officer_state=models.ForeignKey(State,on_delete=models.SET_NULL,null=True)
    subadmin_id=models.ForeignKey(Subadmin,on_delete=models.SET_NULL,null=True)
    
