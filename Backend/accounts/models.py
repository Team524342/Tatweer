# D:\Tatweer\Backend\accounts\models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES=[
         ('product_manager','PRODUCT_MANAGER'),
         ('customer','CUSTOMER'),
         ('admin','Admin'),
         ('inventory_staff','INVENTORY_STAFF'),
         ('order_staff','ORDER_STAFF'),
         ('support_staff','SUPPORT_STAFF'),
     ]
    email = models.EmailField(unique=True, blank=False)
    phone_number = models.CharField(max_length=15, blank=True)
    role=models.CharField(max_length=20,choices=ROLE_CHOICES, default='customer')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username