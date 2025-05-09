from django.shortcuts import render
from .forms import UserRegistrationForm, UserAuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.
def register_view(request, *args, **kwargs):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("login_view"))
    else:
        form = UserRegistrationForm()
    context = {
        "form": form,
    }
    return render(request, "register.html", context)

def login_view(request, *args, **kwargs):
    form = UserAuthenticationForm(request, data=request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            login(request, form.get_user())
            return redirect(reverse("homepage_view"))
    else:
        form = UserAuthenticationForm()

    context = {
        "form" : form,
    }
    return render(request, "login.html", context)