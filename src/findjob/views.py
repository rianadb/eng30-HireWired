import os
from django.shortcuts import render, redirect
from .models import Job, Application
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import JobSearchForm
from django.db.models import Q

@login_required
def find_jobs_view(request, *args, **kwargs):
    jobs = Job.objects.all()
    search_query = request.GET.get("search_query", "")
    location = request.GET.get("location", "")
    min_salary = request.GET.get("min_salary", "")

    # Apply search filter (across category, name, and description)
    if search_query:
        jobs = jobs.filter(
            Q(category__icontains=search_query) |
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)
        )

    # Apply location filter
    if location:
        jobs = jobs.filter(city__icontains=location)

    # Apply salary filter
    if min_salary:
        try:
            min_salary = int(min_salary)
            jobs = jobs.filter(salary__gte=min_salary)
        except ValueError:
            pass  # Ignore invalid inputs gracefully

    # Split the comma-separated details field
    for job in jobs:
        if job.details:
            job.details = job.details.split(",")

    context = {
        "jobs": jobs,
    }
    return render(request, "jobs.html", context)

@login_required
def add_job_view(request):
    if request.method == 'POST' and request.user.user_type == 'employer':
        name = request.POST.get('name')
        description = request.POST.get('description')
        details = request.POST.get('details')
        schedule = request.POST.get('schedule')
        salary = request.POST.get('salary')
        rate_type = request.POST.get('rate_type')
        city = request.POST.get('city')
        Job.objects.create(
            name=name,
            description=description,
            details=details,
            schedule=schedule,
            salary=salary,
            rate_type=rate_type,
            city=city,
        )
    return redirect('find_jobs_view')

def apply_for_job(request):
    if request.method == 'POST':
        full_name = request.POST.get('fullName')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        position = request.POST.get('position')

        resume = request.FILES.get('resume')
        cover_letter = request.FILES.get('coverLetter')

        files_dir = os.path.join(settings.BASE_DIR, 'src', 'files')
        os.makedirs(files_dir, exist_ok=True)  # Ensure the directory exists

        if resume:
            resume_path = os.path.join(files_dir, resume.name)
            with open(resume_path, 'wb+') as destination:
                for chunk in resume.chunks():
                    destination.write(chunk)

        if cover_letter:
            cover_letter_path = os.path.join(files_dir, cover_letter.name)
            with open(cover_letter_path, 'wb+') as destination:
                for chunk in cover_letter.chunks():
                    destination.write(chunk)

        job_id = request.POST.get('job_id')
        print(f"Job ID: {job_id}")
        job = Job.objects.get(id=job_id)
        worker = request.user
        Application.objects.get_or_create(worker=worker, job=job)
        return redirect('find_jobs_view') 

    return redirect('find_jobs_view')
