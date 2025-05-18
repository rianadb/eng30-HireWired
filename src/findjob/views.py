from django.shortcuts import render
from .models import Job

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