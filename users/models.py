from django.db import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.

class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', default="avatars/user.png", blank=True, null=True)