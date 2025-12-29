from dataclasses import fields
from django.contrib.auth import forms as auth_forms
from django import forms as dj_forms
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from .models import User

def validate_img_size(value):
    if value.size > 5*1024*1024:
        raise ValidationError("File size must be less then 5MB!")


class ThinkUserForm(auth_forms.UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Base classes for all text/password inputs
        base_input_class = 'w-full rounded-xl bg-aurora-900/60 border px-3 py-2.5 text-sm text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-aurora-500 focus:border-aurora-500'
        
        for field_name in ['username', 'email', 'password1', 'password2']:
            if field_name in self.fields:
                # Check if field has errors (after form is bound)
                if self.is_bound and field_name in self.errors:
                    self.fields[field_name].widget.attrs['class'] = f'{base_input_class} border-red-500'
                else:
                    self.fields[field_name].widget.attrs['class'] = f'{base_input_class} border-aurora-700'
        
        if 'avatar' in self.fields:
            self.fields['avatar'].widget.attrs.update({
                'class': 'w-full text-xs text-slate-400 file:mr-3 file:px-3 file:py-1.5 file:rounded-md file:border-0 file:text-xs file:font-medium file:bg-aurora-700 file:text-white hover:file:bg-aurora-600',
                'accept': 'image/*'
            })

    avatar = dj_forms.ImageField(
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
            'avatar': dj_forms.FileInput(attrs={
                'class': 'w-full text-xs text-slate-400 file:mr-3 file:px-3 file:py-1.5 file:rounded-md file:border-0 file:text-xs file:font-medium file:bg-aurora-700 file:text-white hover:file:bg-aurora-600',
                'accept': 'image/*'
            }),

            'username':dj_forms.TextInput(attrs={
                'class':'w-full rounded-xl bg-aurora-900/60 border border-aurora-700 px-3 py-2.5 text-sm text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-aurora-500 focus:border-aurora-500 focus:ring-offset-2 focus:ring-offset-slate-900'
            }),

            'email':dj_forms.EmailInput(attrs={
                'class':'w-full rounded-xl bg-aurora-900/60 border border-aurora-700 px-3 py-2.5 text-sm text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-aurora-500 focus:border-aurora-500 focus:ring-offset-2 focus:ring-offset-slate-900'
            }),

            'password1':dj_forms.PasswordInput(attrs={
                'class':'w-full rounded-xl bg-aurora-900/60 border border-aurora-700 px-3 py-2.5 text-sm text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-aurora-500 focus:border-aurora-500 focus:ring-offset-2 focus:ring-offset-slate-900'
            }),

            'password2':dj_forms.PasswordInput(attrs={
                'class':'w-full rounded-xl bg-aurora-900/60 border border-aurora-700 px-3 py-2.5 text-sm text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-aurora-500 focus:border-aurora-500'
            }),
        }


class ThinkAuthForm(auth_forms.AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name in ['username', 'password']:
            if field_name in self.fields:
                self.fields[field_name].widget.attrs.update({
                    'class': 'w-full rounded-xl bg-aurora-900/60 border border-aurora-700 px-3 py-2.5 text-sm text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-aurora-500 focus:border-aurora-500 focus:ring-offset-2 focus:ring-offset-slate-900'
                })

    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username':dj_forms.TextInput(attrs={
                'class': 'w-full rounded-xl bg-aurora-900/60 border border-aurora-700 px-3 py-2.5 text-sm text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-aurora-500 focus:border-aurora-500 focus:ring-offset-2 focus:ring-offset-slate-900'
            }),
            'password':dj_forms.PasswordInput(attrs={
                'class':'w-full rounded-xl bg-aurora-900/60 border border-aurora-700 px-3 py-2.5 text-sm text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-aurora-500 focus:border-aurora-500 focus:ring-offset-2 focus:ring-offset-slate-900'
            })
        }


class ProfileUpdateForm(dj_forms.ModelForm):
    avatar = dj_forms.ImageField(required=False, 
            validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
            validate_img_size],
            help_text='Upload a profile picture (optional, max 5MB)')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'avatar']
        widgets = {
            'avatar': dj_forms.FileInput(attrs={
                'class': 'w-full text-xs text-slate-400 file:mr-3 file:px-3 file:py-1.5 file:rounded-md file:border-0 file:text-xs file:font-medium file:bg-aurora-700 file:text-white hover:file:bg-aurora-600',
                'accept': 'image/*'
            })
        }