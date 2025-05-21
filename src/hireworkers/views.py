from django.shortcuts import render, redirect
from findjob.models import Job, Application
from django.contrib.auth import get_user_model
from .models import Review

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
    reviews = Review.objects.filter(worker=worker).order_by('-created_at')

    if request.method == 'POST' and request.user.is_authenticated:
        # rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        if comment:
            Review.objects.create(
                worker=worker,
                reviewer=request.user,
                # rating=rating,
                comment=comment
            )
        return redirect('hire_worker_profile_view', worker_id=worker_id)
    
    context = {
        'worker': worker,
        'jobs': jobs,
        'reviews': reviews,
    }
    return render(request, 'worker_profile.html', context)