from django.shortcuts import render
from Department.models import Departments
from Branches.models import Branches
# Create your views here.
def home(request):
    depts = Departments.objects.all()  # Get all departments from the database
    branches= Branches.objects.all()
    return render(request,"home.html",{'depts': depts,'branches':branches})