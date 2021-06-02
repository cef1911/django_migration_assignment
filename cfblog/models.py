from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.utils import timezone

# Create your models here.

class School(models.Model):

    name = models.CharField(max_length= 400, default="", null=True)
    def __str__(self):
        return self.name
   

class Certificate_Type(models.Model):
   
    name = models.CharField(max_length= 50)
    def __str__(self):
        return self.name

class Faculty(models.Model):

    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Department(models.Model):

    name = models.CharField(max_length=50)
    faculty = models.ForeignKey(Faculty, on_delete=CASCADE)

    def __str__(self):
        return self.name

class Grade(models.Model):

    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Student(models.Model):
    full_name = models.CharField(max_length= 50, null=True)
    year_of_graduation = models.DateField(default=timezone.now)
    department = models.ForeignKey(Department, on_delete=CASCADE, null=True)
    grade = models.ForeignKey(Grade, on_delete=CASCADE, null=True)
    school = models.ForeignKey(School,on_delete=CASCADE, null=True)
    certificate_type  = models.ForeignKey(Certificate_Type, on_delete=CASCADE, null=True)

    def __str__(self):
        return self.full_name