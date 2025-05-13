from django.shortcuts import render

# Create your views here.
def find_jobs_view(request, *args, **kwargs):
    if request.GET.get("job"):
        ...

    context = {
        # "form" : form,
        # "jobs" : jobs,
    }
    return render(request, "jobs.html", context)