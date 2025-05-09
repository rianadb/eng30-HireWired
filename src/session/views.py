from django.shortcuts import render
from .forms import UserRegistrationForm
# Create your views here.
def register_view(request, *args, **kwargs):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("login_view"))
    else:
        form = UserRegistrationForm()
    context = {
        "form": form,
    }
    return render(request, "register.html", context)

def login_view(request, *args, **kwargs):
    return render(request, "login.html", {})