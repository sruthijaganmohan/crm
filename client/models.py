from django.db import models
from django.contrib.auth import get_user_model
from team.models import Team

User = get_user_model()

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    description = models.TextField(blank=True, null=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
    created_by = models.ForeignKey(User, related_name='clients', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    content = models.TextField(blank=True, null=True) 
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='client_comments', null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    created_by = models.ForeignKey(User, related_name='client_comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Contact(models.Model):
    subject = models.CharField(max_length=1000)
    content = models.TextField(blank=True, null=True) 

    def __str__(self):
        return self.subject