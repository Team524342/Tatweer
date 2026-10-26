from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField(blank=True)
    brand=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField()
    sku=models.CharField(max_length=30,unique=True)
    image=models.ImageField(upload_to='products/',blank=True,null=True)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name