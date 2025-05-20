"""
URL configuration for hirewired project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from pages.views import homepage_view, about_view, logout_view
from session.views import register_worker_view, register_employer_view, login_view, register_view
from findjob.views import find_jobs_view
from hireworkers.views import hire_workers_view
from profiles.views import edit_profile_view, edit_employer_profile_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage_view, name='homepage_view'),
    path('about/', about_view, name='about_view'),
    path('register/', register_view, name='register_view'),
    path('register/worker/', register_worker_view, name='register_worker_view'),
    path('register/employer/', register_employer_view, name='register_employer_view'),
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),
    path('jobs/', find_jobs_view, name='find_jobs_view'),
    path('workers/', hire_workers_view, name='hire_workers_view'),
    path('profile/worker/', edit_profile_view, name='edit_profile_view'),
    path('profile/employer/', edit_employer_profile_view, name='edit_employer_profile_view'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
