from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='team_manager')
    member1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='team_member1', null=True, blank=True)
    member2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='team_member2', null=True, blank=True)
    member3 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='team_member3', null=True, blank=True)
    member4 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='team_member4', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name