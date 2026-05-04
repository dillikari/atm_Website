from django.db import models
from django.core import validators
# Create your models here.

class CustomerAccount(models.Model):
    account_Number=models.IntegerField(primary_key=True)
    customer_Name=models.CharField(max_length=50)
    pin_Number=models.IntegerField(
       validators=[
            validators.MinValueValidator(0),
            validators.MaxValueValidator(9999)
        ]
    )
    customer_Age=models.IntegerField()
    mobile_Number=models.IntegerField()
    customer_Aadhaar=models.IntegerField()
    customer_Address=models.CharField(max_length=200)
    customer_State=models.CharField(max_length=100)
    balanceAmount=models.DecimalField(max_digits=20,decimal_places=2,default=0)


