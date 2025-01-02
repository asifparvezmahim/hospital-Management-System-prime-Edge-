"""
URL configuration for Main_Project_File project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Home.views import home
from Department.views import all_departments
from Doctors.views import doctor_list,get_an_appointment
from Accounts.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name="home"),
    path("departments/",all_departments),
    path("doctors/",doctor_list,name="doctors"),
    path("doctor/get_appointment/<int:id>/",get_an_appointment,name="get_an_appointment"),
    path("login/",login,name="login")
]
urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)