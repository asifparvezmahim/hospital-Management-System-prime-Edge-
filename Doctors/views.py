from django.shortcuts import render
from datetime import datetime,timedelta
from Doctors.models import Doctor
from Doctors.models import Weekly_Days
from Doctors.models import Designation
from Department.models import Departments
from Branches.models import Branches

# Create your views here.
def doctor_list(request):
    filteredDoctors = Doctor.objects.all()
    is_filtered = False  
    if request.method == "POST":
        branch = request.POST.get("branch")
        designation = request.POST.get("designation")
        specialities = request.POST.get("specialities")       
        if branch:
            try:               
                branch_instance = Branches.objects.get(name=branch)
                filteredDoctors = filteredDoctors.filter(branch=branch_instance) 
            except Branches.DoesNotExist:
                print(f"Branch {branch} not found.")        
        if designation:
            try:        
                designation_instance = Designation.objects.get(name=designation)
                filteredDoctors = filteredDoctors.filter(designation=designation_instance)  
            except Designation.DoesNotExist:
                print(f"Designation {designation} not found.")      
        if specialities:
            try:               
                speciality_instance = Departments.objects.get(name=specialities)
                filteredDoctors = filteredDoctors.filter(specialities=speciality_instance) 
            except Departments.DoesNotExist:
                print(f"Speciality {specialities} not found.")
        is_filtered = True
         
    
      
    depts = Departments.objects.all()  
    branches = Branches.objects.all()  
    days = Weekly_Days.objects.all()  
    dsgntns = Designation.objects.all()  
    return render(request, "filteredDoctor.html", {
        'depts': depts, 'branches': branches, 'days': days, 'dsgntns': dsgntns, 'filteredDoctors': filteredDoctors,
        "is_filtered": is_filtered
    })



def get_an_appointment(request,id):
    depts = Departments.objects.all()  
    branches = Branches.objects.all()  
    days = Weekly_Days.objects.all()  
    dsgntns = Designation.objects.all() 
    selected_doctor = Doctor.objects.get(id=id)
    practice_days_of_selected_doctors = selected_doctor.practice_day.all()
    practice_day = []
    next_seven_days ={}
    #get current date
    current_date = datetime.now()
    count = 0


    for day in practice_days_of_selected_doctors:
        practice_day.append(day.name)
    
    for i in range(1,1000):
        future_date = current_date + timedelta(days=i)  # Add `i` days to the current date
        date_str = future_date.strftime("%Y-%m-%d")     # Format the date as YYYY-MM-DD
        day_name = future_date.strftime("%A")           # Get the full day name
        
        if day_name in practice_day:
            next_seven_days[date_str] = day_name
            count+=1

            if count==7:
                break
    print(next_seven_days)

    
    return render(request,"get_an_appointment.html",{"depts":depts,"branches":branches,"days":days,"dsgntns":dsgntns,"selected_doctor":selected_doctor})