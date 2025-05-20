from django.shortcuts import render
from .forms import UserRegistrationForm, UserAuthenticationForm, EmployerRegistrationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.
def register_view(request, *args, **kwargs):
    return render(request, "register.html", {})

def register_worker_view(request, *args, **kwargs):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = "worker"
            # user.set_password(form.cleaned_data['password'])

            user.save()
            login(request, user)
            return redirect(reverse("homepage_view"))
    else:
        form = UserRegistrationForm()
    context = {
        "form": form,
    }
    return render(request, "register_worker.html", context)

def register_employer_view(request, *args, **kwargs):
    if request.method == "POST":
        form = EmployerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = "employer"
            # user.set_password(form.cleaned_data['password'])

            user.save()
            login(request, user)
            return redirect(reverse("homepage_view"))
    else:
        form = EmployerRegistrationForm()
    context = {
        "form": form,
    }
    return render(request, "register_employer.html", context)

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