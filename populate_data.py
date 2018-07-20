import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

import random
from first_app.models import Student, School
from faker import Faker

fakegen = Faker()
schools = ['DPS', 'AVN', 'BPS', 'SMS', 'VMPS']
fake_address = fakegen.address()
fake_email = fakegen.email()
fake_number = fakegen.building_number()

def add_school():
    s = School.objects.get_or_create(name=random.choice(schools), address=fake_address, email=fake_email, phone_number=fake_number)[0]
    s.save()
    return s

def populate(N=5):
    for entry in range(N):
        school = add_school()
        fake_name = fakegen.name()
        fake_age = fakegen.phone_number()

        student = Student.objects.get_or_create(name=fake_name, age=fake_age, school=school)


if __name__ == '__main__':
    print("Populating data... Please wait...")
    populate(20)
    print("Populating complete!")