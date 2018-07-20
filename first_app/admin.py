from django.contrib import admin

# Register your models here.
from first_app.models import School, Student

admin.site.register(School)
admin.site.register(Student)