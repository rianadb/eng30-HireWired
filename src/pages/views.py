from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import logout
from findjob.models import Application  # import at the top

# Create your views here.
def homepage_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        return redirect('dashboard_view')

    return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})

def logout_view(request, *args, **kwargs):
    if request.method == "POST":
        logout(request)
        return redirect(reverse("homepage_view"))
    
    else:
        return redirect(reverse("homepage_view"))

def dashboard_view(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('homepage_view')

    if request.user.user_type == "worker":
        applications = Application.objects.filter(worker=request.user).select_related('job')
        
        context = {
            "applications": applications
        }
        return render(request, "dashboard_worker.html", context)

    elif request.user.user_type == "employer":
        return render(request, "dashboard_employer.html")

    return redirect('homepage_view')