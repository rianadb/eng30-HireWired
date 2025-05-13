from django.shortcuts import render

# Create your views here.
def find_jobs_view(request, *args, **kwargs):
    return render(request, "jobs.html", {})