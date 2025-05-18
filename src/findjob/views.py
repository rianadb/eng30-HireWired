from django.shortcuts import render
from .models import Job

from .forms import JobSearchForm

# Create your views here.
def find_jobs_view(request, *args, **kwargs):
    jobs = Job.objects.all()
    

    context = {
        # "form" : form,
        "jobs" : jobs,
    }
    return render(request, "jobs.html", context)