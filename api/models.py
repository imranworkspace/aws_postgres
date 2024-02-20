from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name=models.CharField(max_length=15)
    email=models.EmailField()
    profile_pic = models.ImageField(upload_to='images/', default='', null=True, blank=True)
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table="students"