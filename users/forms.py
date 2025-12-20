from django.contrib.auth import forms
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from .models import User
from django.db import models

def validate_img_size(value):
    if value.size > 5*1024*1024:
        raise ValidationError("File size must be less then 5MB!")


class ThinkUserForm(forms.UserCreationForm):
    avatar = models.ImageField(
        required=False, validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']), validate_img_size
            ]
        )
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'avatar']