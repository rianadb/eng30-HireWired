from django import forms
# from django.contrib.auth.models import User
from session.models import User
from .models import WorkerProfile, EmployerProfile

class UserForm(forms.ModelForm):
    first_name = forms.CharField(
        label="First Name",
        widget=forms.TextInput(attrs={"placeholder": "First Name", "class": "form-control" }), 
        required=False)
    last_name = forms.CharField(
        label="Last Name",
        widget=forms.TextInput(attrs={"placeholder": "Last Name", "class": "form-control" }), 
        required=False)
    
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(
            attrs={"placeholder": "juandelacruz@gmail.com", "class": "form-control"}
        )
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
        ]

class UserProfileForm(forms.ModelForm):
    contact_number = forms.CharField(
        label="Contact Number",
        widget=forms.TextInput(attrs={"placeholder": "Contact Number", "class": "form-control" }), 
        required=False)
    
    experience = forms.CharField(
        label="Experience",
        widget=forms.Textarea(attrs={"placeholder": "Experience", "class": "form-control" }), 
        required=False)

    details = forms.CharField(
        label="Details",
        widget=forms.Textarea(attrs={"placeholder": "Details", "class": "form-control" }), 
        required=False)

    profile_picture = forms.ImageField(
        widget=forms.FileInput(attrs={"class": "form-control" }), 
        required=False)

    certification = forms.FileField(
        label="Certification",
        widget=forms.FileInput(attrs={"class": "form-control" }), 
        required=False)

    class Meta:
        model = WorkerProfile
        fields = [
            'experience',
            'details',
            'certification',
            'profile_picture',
        ]

class EmployerProfileForm(forms.ModelForm):
    contact_number = forms.CharField(
        label="Contact Number",
        widget=forms.TextInput(attrs={"placeholder": "Contact Number", "class": "form-control" }), 
        required=False)

    details = forms.CharField(
        label="Details",
        widget=forms.Textarea(attrs={"placeholder": "Details", "class": "form-control" }), 
        required=False)

    profile_picture = forms.ImageField(
        widget=forms.FileInput(attrs={"class": "form-control" }), 
        required=False)

    addtl_docs = forms.FileField(
        label="Additional Documents",
        widget=forms.FileInput(attrs={"class": "form-control" }), 
        required=False)

    class Meta:
        model = EmployerProfile
        fields = [
            'details',
            'addtl_docs',
            'profile_picture',
        ]