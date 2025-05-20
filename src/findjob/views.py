from django.shortcuts import render, redirect
from .models import Job
import os
from django.conf import settings
from .forms import JobSearchForm

# Create your views here.
def find_jobs_view(request, *args, **kwargs):

    jobs = Job.objects.all()
    search_query = request.GET.get("search_query")

    if search_query:
        jobs = jobs.filter(category__icontains=search_query) or jobs.filter(name__icontains=search_query) or jobs.filter(description__icontains=search_query)

    for job in jobs:
        if job.details:
            details = job.details.split(",")
            job.details = details
        

    context = {
        # "form" : form,
        "jobs" : jobs,
    }
    return render(request, "jobs.html", context)


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

        # Optionally, log or save application data to a model

        return redirect('find_jobs_view')  # Redirect back to the jobs page

    return redirect('find_jobs_view')
