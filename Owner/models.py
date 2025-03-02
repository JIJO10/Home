from django.db import models
from Admin.models import RentType
from guest.models import Owner

# Create your models here.


class Rent(models.Model):
    rent_name=models.CharField(max_length=50)
    rent_image=models.FileField(upload_to='rentdocs/')
    rent_details=models.TextField(null=True)
    rent_amount=models.CharField(max_length=50)
    rent_vsts=models.IntegerField(default=0)
    renttype_id=models.ForeignKey(RentType,on_delete=models.SET_NULL,null=True)
    owner_id=models.ForeignKey(Owner,on_delete=models.SET_NULL,null=True)
    
class Gallery(models.Model):
    gallery_image=models.FileField(upload_to='gallerydocs/')
    rent_id=models.ForeignKey(Rent,on_delete=models.SET_NULL,null=True)
