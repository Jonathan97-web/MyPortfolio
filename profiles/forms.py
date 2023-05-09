from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(
                              required=True
                              )

    class Meta:
        model = User
        fields = ['email']


class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'intro', 'image']
