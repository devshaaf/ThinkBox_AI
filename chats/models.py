from django.contrib.auth.models import User
from django.db import models
from users.models import User
from workspaces.models import WorkSpace

# Create your models here.


class ChatSession(models.Model):
    workspace = models.ForeignKey(WorkSpace, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


class ChatMessage(models.Model):

    class ChatRoles(models.TextChoices):
        USER = 'USER', 'User'
        ASSISTANT = 'ASSISTANT', 'Assistant'
        
    session = models.ForeignKey(ChatSession, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ChatRoles.choices)
    message = models.TextField()
    retrieved_chunks = models.JSONField(null=True)
    tokens_used = models.IntegerField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)