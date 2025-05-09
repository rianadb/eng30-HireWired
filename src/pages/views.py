from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import logout

# Create your views here.
def homepage_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})

def logout_view(request, *args, **kwargs):
    if request.method == "POST":
        logout(request)
        return redirect(reverse("homepage_view"))
    
    else:
        return redirect(reverse("homepage_view"))