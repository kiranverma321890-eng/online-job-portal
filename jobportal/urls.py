"""
URL configuration for jobportal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from mainapp import views
from adminapp.views import *
from userapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('about/', views.about, name='about'),
    path('jobs/', views.jobs, name='jobs'),
    path('contact/',views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name= 'register'),
    path('admindash/',admindash, name='admindash') , 
    path('adminlogout/',adminlogout, name='adminlogout'),
    path('faq/',views.faq, name='faq'),  
    path('jobseeker/',jobseeker, name="jobseeker"),
    path('postjob/',postjob, name="postjob"),
    path('postedjob/',postedjob, name="postedjob"),
    path('enquiries/',enquiries, name="enquiries"),
    path('changeadminpwd/',changeadminpwd, name="changeadminpwd"),
    #userapp urls
    path('userdash/',userdash,name='userdash'),
    path('userlogout/',userlogout,name='userlogout'),
    path('viewjobs/',viewjobs,name='viewjobs'),
    path('changeuserpwd/',changeuserpwd, name="changeuserpwd"),
    
    path('giveresponse/',giveresponse, name="giveresponse"),
    path('viewfeedback/',viewfeedback, name="viewfeedback"),
    path('viewcomplaint/',viewcomplaint, name="viewcomplaint"),
    path('deleteenq<id>/',deleteenq, name="deleteenq"),
      
]
