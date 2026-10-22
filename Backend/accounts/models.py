from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    ROLE_CHOICES=[
        ('product_manger','Product_Manager'),
        ('customer',"Customer"),
        ('admin','Admin'),
        ('inventory_staff',"Inventory_Staff"),
        ('order_staff','Order_Staff'),
        ('support_staff',"Support_Staff")

    ]
    phone_number=models.CharField(max_length=15,blank=True)
    email=models.EmailField(unique=True)
    role=models.CharField(max_length=20,choices=ROLE_CHOICES)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.username

