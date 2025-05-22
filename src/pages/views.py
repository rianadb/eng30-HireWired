from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import logout
from findjob.models import Job, Application

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
        # if hasattr(request.user, 'user_type') and request.user.user_type == 'employer':
        if request.method == "POST":
            app_id = request.POST.get("application_id")
            action = request.POST.get("action")
            try:
                application = Application.objects.get(id=app_id, job__employer=request.user)
                if action == "accept":
                    application.status = "accepted"
                elif action == "reject":
                    application.status = "rejected"
                application.save()
            except Application.DoesNotExist:
                pass  # Optionally handle error

            return redirect('dashboard_view')
            
        jobs = Job.objects.filter(employer=request.user)
        jobs_with_applicants = []
        for job in jobs:
            applications = Application.objects.filter(job=job).select_related('worker')
            jobs_with_applicants.append({
                'job': job,
                'applications': applications,
            })
        context = {
            'jobs_with_applicants': jobs_with_applicants,
        }
        
        return render(request, "dashboard_employer.html", context)

    return redirect('homepage_view')