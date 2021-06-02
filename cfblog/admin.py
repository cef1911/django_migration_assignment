from django.contrib import admin
from .models import School, Student, Certificate_Type, Department, Grade, Faculty

# Register your models here.

admin.site.register(School)
admin.site.register(Student)
admin.site.register(Certificate_Type)
admin.site.register(Department)
admin.site.register(Grade)
admin.site.register(Faculty)