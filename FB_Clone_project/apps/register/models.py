from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser


gen = (("Female", 'Female'),
        ("Male", 'Male'),
        ("Custom", 'Custom'),)

class CustomUser(AbstractUser):
    mobile = models.CharField( max_length=60)
    age = models.IntegerField(blank=True,null=True)
    DOB = models.DateField(auto_now_add=False,blank=True,null=True)
    gender = models.CharField(max_length=60, choices=gen)
    # password = models.CharField(max_length=128,blank=False,null=False) # Adjusted max_length for password minimum is 128
    
    def __str__(self):
        return self.first_name
