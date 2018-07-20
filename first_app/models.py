from django.db import models
# Create your models here.


class School(models.Model):
    name = models.CharField(max_length=250, blank=False)
    address = models.CharField(max_length=500, blank=False)
    email = models.EmailField(blank=False)
    phone_number = models.CharField(blank=False, max_length=15)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=50, blank=False)
    age = models.CharField(blank=False, max_length=3)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.name