from django.shortcuts import render

# Create your views here.
from first_app.models import Student


def index(request):
    students = Student.objects.all()
    mycontext = {
        'students' : students
    }
    return render(request, 'first_app/index.html', mycontext)