from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('seller', 'Seller'),
        ('buyer', 'Buyer'),
    ]
    role = models.CharField(max_length=100, choices=ROLE_CHOICES, default='buyer')
    phone = models.CharField(max_length=10)
    email = models.EmailField(null=True, blank=True)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - {self.role}"