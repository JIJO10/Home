from django.db import models
from guest.models import*
from Subadmin.models import Officer
from Owner.models import Rent

# Create your models here.

class Complaint(models.Model):
    complaint_title=models.CharField(max_length=50)
    complaint_content=models.TextField(null=True)
    complaint_date=models.DateField(auto_now=True)
    complaint_replay=models.TextField(null=True)
    complaint_status=models.IntegerField(default=0)
    user_id=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    owner_id=models.ForeignKey(Owner,on_delete=models.SET_NULL,null=True)
    officer_id=models.ForeignKey(Officer,on_delete=models.SET_NULL,null=True)

class Feedback(models.Model):
    feedback_content=models.TextField(null=True)
    feedback_date=models.DateField(auto_now=True,null=True)
    user_id=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    owner_id=models.ForeignKey(Owner,on_delete=models.SET_NULL,null=True)
    officer_id=models.ForeignKey(Officer,on_delete=models.SET_NULL,null=True)

class Booking(models.Model):
    booking_fromdate=models.DateField()
    booking_todate=models.DateField()
    booking_date=models.DateField(auto_now=True)
    booking_status=models.IntegerField(default=0)
    payment_status=models.IntegerField(default=0)
    user_id=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    rent_id=models.ForeignKey(Rent,on_delete=models.SET_NULL,null=True)