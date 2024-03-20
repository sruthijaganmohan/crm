from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}"