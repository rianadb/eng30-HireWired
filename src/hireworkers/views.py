from django.shortcuts import render
from findjob.models import Job, Application
from django.contrib.auth import get_user_model

# Create your views here.
def hire_workers_view(request, *args, **kwargs):
    search_query = request.GET.get("search_query")

    categories = Job.objects.values_list('category', flat=True).distinct()
    categories = list(categories)
    selected_category = request.GET.get('category') or (categories[0] if categories else None)
    print(selected_category)

    applications = []
    if selected_category:
        jobs_in_category = Job.objects.filter(category=selected_category)
        applications = Application.objects.filter(job__in=jobs_in_category)
        # worker_ids = applications.values_list('worker_id', flat=True).distinct()
        # workers = get_user_model().objects.filter(id__in=worker_ids)

        if search_query:
            applications = (
                applications.filter(worker__workerprofile__experience__icontains=search_query)
                | applications.filter(job__name__icontains=search_query)
                | applications.filter(job__description__icontains=search_query)
            )
    
    context = {
        'categories': categories,
        'selected_category': selected_category,
        # 'workers': workers,
        'applications': applications,
    }
    return render(request, 'workers.html', context)

def hire_worker_profile_view(request, worker_id):
    worker = get_user_model().objects.get(id=worker_id)
    applications = Application.objects.filter(worker=worker)
    jobs = [application.job for application in applications]

    context = {
        'worker': worker,
        'jobs': jobs,
    }
    return render(request, 'worker_profile.html', context)