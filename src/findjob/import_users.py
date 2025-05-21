import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pandas as pd
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hirewired.settings')
django.setup()

from session.models import User
from findjob.models import Job, Application
from profiles.models import WorkerProfile, Category

csv_file_path = os.path.join(os.path.dirname(__file__), '../data/sample_users.csv')
df = pd.read_csv(csv_file_path)

print(df.head())

for _, row in df.iterrows():
    user, created = User.objects.get_or_create(
        username=row['username'],           
        password='password',
        user_type='worker',
        first_name=row['first_name'],
        last_name=row['last_name'],
        email=row['email'],
        contact_number=row['contact_number'],
    )

    profile, created = WorkerProfile.objects.get_or_create(
        user=user,
        defaults={
            'experience': row['experience'],
            'details': row['details'],
        }
    )
    if not created:
        profile.experience = row['experience']
        profile.details = row['details']
        profile.save()

    try:
        job = Job.objects.get(name=row['job_title'])
        # if hasattr(profile, 'categories'):
        category_obj, _ = Category.objects.get_or_create(name=job.category)
        profile.categories.add(category_obj)
        Application.objects.create(worker=user, job=job)
        print(f"Application created for {user.username} for job '{job.name}'")

    except Job.DoesNotExist:
        print(f"Job '{row['job_title']}' not found for user {user.username}")

print("Users imported!")


