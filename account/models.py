from django.db import models
from django.contrib.auth import get_user_model
from team.models import Team

User = get_user_model()

# Create your models here.
class Account(models.Model):
    MANAGER = 'Manager'
    ASSOCIATE = 'Associate'

    ROLE_CHOICES = [
        ('MANAGER', 'Manager'),
        ('ASSOCIATE', 'Associate'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default=ASSOCIATE)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.username