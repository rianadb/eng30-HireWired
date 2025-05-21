from django.shortcuts import render, redirect
# Create your views here.
from django.contrib.auth.decorators import login_required
from .forms import UserForm, UserProfileForm, EmployerProfileForm
from .models import WorkerProfile

@login_required
def edit_profile_view(request):
    user = request.user
    profile, created = WorkerProfile.objects.get_or_create(user=user)  # Ensures proper profile

    if request.method == "POST":
        user_form = UserForm(request.POST, instance=user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid() and user_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('edit_profile_view')
    else:
        user_form = UserForm(instance=user)
        profile_form = UserProfileForm(instance=profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'profile_worker.html', context)


@login_required
def edit_employer_profile_view(request):
    user = request.user
    profile = request.user.profile
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = EmployerProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid() and user_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('edit_employer_profile_view')
    else:
        user_form = UserForm(instance=user)
        profile_form = EmployerProfileForm(instance=profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        }
    return render(request, 'profile_employer.html', context)