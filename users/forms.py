from django.contrib.auth import forms
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from .models import User

def validate_img_size(value):
    if value.size > 5*1024*1024:
        raise ValidationError("File size must be less then 5MB!")


class ThinkUserForm(forms.UserCreationForm):
    avatar = forms.forms.ImageField(
        required=False,
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
            validate_img_size
        ],
        help_text='Upload a profile picture (optional, max 5MB)'
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'avatar']
        widgets = {
            'avatar': forms.forms.FileInput(attrs={
                'class': 'w-full text-xs text-slate-400 file:mr-3 file:px-3 file:py-1.5 file:rounded-md file:border-0 file:text-xs file:font-medium file:bg-aurora-700 file:text-white hover:file:bg-aurora-600',
                'accept': 'image/*'
            })
        }