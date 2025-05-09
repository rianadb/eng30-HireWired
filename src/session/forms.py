from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError

class UserRegistrationForm(UserCreationForm):
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Last Name", "class": "form-control" })
        )
    first_name = forms.CharField(
        max_length=30, 
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "First Name", "class": "form-control" }))
    
    username = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Username", "class": "form-control" }))

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"placeholder": "juandelacruz@gmail.com", "class": "form-control"}
        )
    )

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password", "class": "form-control"}
        ),
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={"placeholder": "Re-enter Password", "class": "form-control"}
        ),
    )

    class Meta:
        model = User
        fields = [
            "last_name",
            "first_name",
            "username",
            "email",
            "password1",
            "password2",
        ]


class UserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Username", "class": "form-control" }))

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password", "class": "form-control"}
        ),
    )