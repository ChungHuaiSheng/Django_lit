from django.db import models
from django.contrib import admin


# Create your models here.
class Vendor(models.Model):
    vendor_name = models.CharField(max_length=20)
    store_name = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.vendor_name


class Food(models.Model):
    food_name = models.CharField(max_length=30)
    price_name = models.DecimalField(max_digits=3, decimal_places=0)
    food_vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)

    def __str__(self):
        return self.food_name


class VendorAdmin(admin.ModelAdmin):
    list_display = ('id', 'vendor_name')
