from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=False, blank=False, on_delete=models.CASCADE)

    phone_field = models.CharField(max_length=12, blank=False)

    def __str__(self):
        return self.user.username


class Contact_us(models.Model):
    name = models.CharField(max_length=100, null=True)
    subject = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.email
