from django.db import models
from Department.models import Departments
from Branches.models import Branches

# Create your models here.
class Weekly_Days(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
       return self.name
    
class Designation (models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
       return self.name
    
class Doctor (models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to="Doctors/images/")
    designation = models.ForeignKey(Designation,on_delete=models.CASCADE)
    specialities = models.ManyToManyField(Departments,related_name="doctors")
    branch = models.ManyToManyField(Branches,related_name="doctors")
    degree = models.TextField(max_length=10000)
    practice_day = models.ManyToManyField(Weekly_Days,related_name="doctors")
    
    def __str__(self):
        return self.name