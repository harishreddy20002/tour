from django.db import models
from django.db import models
from rest_framework_api_key.models import AbstractAPIKey

class Organization(models.Model):
    name = models.CharField(max_length=128)
    active = models.BooleanField(default=True)

class OrganizationAPIKey(AbstractAPIKey):
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="api_keys",
    )
class REG(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)

class PLACE(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    activity= models.CharField(max_length=100,default="null")
    latitude = models.CharField(max_length=100)
    logitude = models.CharField(max_length=100)
    rating= models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
