import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hirewired.settings')
django.setup()

from profiles.models import Category

category_names = [
    "Skilled Work",
    "Logistics",
    "Construction",
    "Technical Support",
    "Agriculture and Groundskeeping",
    "Building and Grounds Maintenance",
]

for name in category_names:
    Category.objects.get_or_create(name=name)
print("Categories created!")


