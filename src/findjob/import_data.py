import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pandas as pd
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hirewired.settings')
django.setup()

from findjob.models import Job

csv_file_path = os.path.join(os.path.dirname(__file__), '../data/sample_jobs.csv')
df = pd.read_csv(csv_file_path)

print(df.head())

for _, row in df.iterrows():
    Job.objects.create(
        name=row['Job Title'],           
        description=row['Description'],
        category=row['Category'],
        schedule=row['Typical Daily Schedule'],
        salary=row['Approx. Hourly Rate (PHP)'],
        details=row['Details'],
    )

print("Jobs imported!")