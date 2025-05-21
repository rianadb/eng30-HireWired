from django.shortcuts import render, redirect
from findjob.models import Job, Application
from django.contrib.auth import get_user_model
from .models import Review
from profiles.models import Category

def hire_workers_view(request, *args, **kwargs):
    selected_location = request.GET.get("location")
    categories = Category.objects.all()
    selected_category = request.GET.get('category') or (categories[0].name if categories else None)

    workers = []
    if selected_category:
        workers = get_user_model().objects.filter(
            workerprofile__categories__name=selected_category
        ).distinct()

        if selected_location:
            workers = workers.filter(workerprofile__location__icontains=selected_location)

    # Clean locations
    locations = get_user_model().objects.filter(
        workerprofile__categories__name=selected_category
    ).exclude(workerprofile__location__isnull=True) \
     .exclude(workerprofile__location__exact='') \
     .values_list('workerprofile__location', flat=True).distinct()

    context = {
        'categories': categories,
        'selected_category': selected_category,
        'workers': workers,
        'locations': locations,
        'selected_location': selected_location,
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