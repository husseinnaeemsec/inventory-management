from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission

User = get_user_model()
class Inventory(models.Model):
    
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=150)

class Role(models.Model):
    ROLES = (
        ("admin","Administrator"),
        ("manager","Manager"),
        ("staff","Staff"),
    )
    inventories = models.ManyToManyField(Inventory)
    name = models.CharField(max_length=150)
    permissions = models.ManyToManyField(Permission)

class UserRole(models.Model):
    inventory = models.ForeignKey(Inventory,on_delete=models.CASCADE,related_name='user_roles')
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='roles')
    role = models.ForeignKey(Role, on_delete=models.CASCADE,related_name='users')

