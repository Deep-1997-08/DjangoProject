from django.db import models

# Create your models here.
class UserDetails(models.Model):
    username=models.CharField(max_length =100, primary_key=True)
    email= models.EmailField()
    password=models.CharField(max_length=12,blank=True)
    