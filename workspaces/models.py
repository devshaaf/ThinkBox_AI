from enum import unique
from random import choices
from django.db import models
from users.models import User

# Create your models here.


class WorkSpace(models.Model):
    name = models.CharField(max_length=150, blank=True, unique=True, default='My Workspace')
    description = models.TextField(blank=True, null=True, help_text='Optional')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class WorkSpaceMember(models.Model):

    class Role(models.TextChoices):
        OWNER = 'OWNER', 'Owner'
        ADMIN = 'ADMIN', 'Admin'
        EDITOR = 'EDITOR', 'Editor'
        VIEWER = 'VIEWER', 'Viewer'

    workspace = models.ForeignKey(WorkSpace, on_delete=models.CASCADE) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=Role.choices)
    permissions = models.JSONField(default=dict)
    joined_at = models.DateTimeField(auto_now_add=True)