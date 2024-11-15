from django.db import models

from django.contrib.auth.models import AbstractUser

class UserManagement(AbstractUser):

    phone=models.CharField(max_length=20,unique=True)

class ExpenseManagement(models.Model):

    title=models.CharField(max_length=200)

    category=(
        ("food","food"),
        ("travel","travel"),
        ("entertaiment","entertaiment"),
        ("other","other")
    )

    category_option=models.CharField(max_length=200,choices=category,default="food")

    amount=models.PositiveIntegerField()

    payment=(
        ("Card","Card"),
        ("Cash","Cash"),
        ("UPI","UPI")
    )

    payment_option=models.CharField(max_length=200,choices=payment,default="card")

    def __str__(self):
        
        return self.title




