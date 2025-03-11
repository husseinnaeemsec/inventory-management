from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    # Add custom fields here
    bio = models.TextField(max_length=1000)
    

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=150, null=True)
    phone = models.CharField(max_length=15,null=True)
    email = models.EmailField(unique=True,null=True)
    address = models.CharField(max_length=255,null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    is_active = models.BooleanField(default=True)

    
    def __str__(self):
        return self.name