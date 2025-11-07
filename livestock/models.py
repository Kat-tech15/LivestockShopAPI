from django.db import models
from accounts.models import CustomUser

class Livestock(models.Model):
    CATEGORY_CHOICES = [
        ('cattle', 'Cattle'),
        ('goat', 'Goat'),
        ('donkey', 'Donkey'),
        ('pig', 'Pig'),
        ('poultry', 'Poultry')
    ]
    owner = models.ForeignKey(CustomUser, on_delete=models.CASACADE)
    name  = models.CharField(max_length=50)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    image  = models.ImageField(upload_to='livestock_images/', null=True, blank=True)
    age  = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.category}"