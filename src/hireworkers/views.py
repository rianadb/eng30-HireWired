from django.shortcuts import render

# Create your views here.
def hire_workers_view(request, *args, **kwargs):
    return render(request, "workers.html", {})