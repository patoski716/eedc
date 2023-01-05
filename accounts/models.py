from django.db import models
from shortuuidfield import ShortUUIDField

# Create your models here.

class Customer(models.Model):
    c_phone=models.CharField(max_length=255, null=True)
    c_address=models.CharField(max_length=255, null=True)
    c_name=models.CharField(max_length=255, null=True)
    date_added= models.DateTimeField(auto_now_add=True)  

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.c_phone

class Payment(models.Model):
    token=ShortUUIDField()
    c_phone=models.CharField(max_length=255, null=True,default='')
    amount=models.CharField(max_length=255, null=True)
    date_added= models.DateTimeField(auto_now_add=True)  


    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.token