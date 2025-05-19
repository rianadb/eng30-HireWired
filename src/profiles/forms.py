from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "First Name", "class": "form-control" }), 
        required=False)
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Last Name", "class": "form-control" }), 
        required=False)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
        ]

class UserProfileForm(forms.ModelForm):
    experience = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Experience", "class": "form-control" }), 
        required=False)

    details = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Details", "class": "form-control" }), 
        required=False)
    
    class Meta:
        model = Profile
        fields = [
            'experience',
            'details',
            'certification',
            'profile_picture',
        ]