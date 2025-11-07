from django.db import models
from accounts.models import CustomUser
from livestock.models import Livestock

class Review(models.Model):
    reviewer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    livestock = models.ForeignKey(Livestock, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reviewer} - {self.livestock}"
