from django.db import models

# Create your models here.

class Country(models.Model):
    country_name=models.CharField(max_length=50)

    def __str__(self):
        return self.country_name


class RentType(models.Model):
    renttype_name=models.CharField(max_length=50)

    def __str__(self):
        return self.renttype_name


class State(models.Model):
    state_name=models.CharField(max_length=50)
    country=models.ForeignKey(Country,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.state_name

class District(models.Model):
    district_name=models.CharField(max_length=50)
    state=models.ForeignKey(State,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.district_name


class Place(models.Model):
    place_name=models.CharField(max_length=50)
    district=models.ForeignKey(District,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.place_name

class Subadmin(models.Model):
    subadmin_name=models.CharField(max_length=50)
    subadmin_contact=models.CharField(max_length=50)
    subadmin_email=models.EmailField(unique=True)
    subadmin_address=models.TextField(null=True)
    subadmin_photo=models.FileField(upload_to='subadmindocs/')
    subadmin_pwd=models.CharField(max_length=50,unique=True)
    subadmin_doj=models.DateField(auto_now=True)
    subadmin_country=models.ForeignKey(Country,on_delete=models.SET_NULL,null=True)

class Admin(models.Model):
    admin_name=models.CharField(max_length=50)
    admin_email=models.EmailField(unique=True)
    admin_pwd=models.CharField(max_length=50,unique=True)