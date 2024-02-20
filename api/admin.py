from django.contrib import admin

# Register your models here.
from .models import StudentModel
@admin.register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','email','profile_pic']