from django.shortcuts import render,redirect
from django.contrib import messages
from mainapp.models import JobSeeker, LoginInfo
from . models import JobInfo
import datetime

# Create your views here.
def admindash(request):
    try:
        if request.session['adminid'] !=  None:
            return render(request,'admindash.html')
    except KeyError:
        messages.error(request,'Please Login')
        return redirect('login')

def adminlogout(request):
    try:
        if request.session['adminid'] != None:
            del request.session['adminid']
            messages.error(request,"You have logged-out successfully")
            return redirect('login')
    except KeyError:
        messages.error(request,'Please Login')
        return redirect('login')

def jobseeker(request):
    try:
        if request.session['adminid'] !=  None:
            js = JobSeeker.objects.all()
            return render(request,'jobseeker.html', {"js":js})
    except KeyError:
        messages.error(request,'Please Login')
        return redirect('login')

def postjob(request):
    try:
        if request.session['adminid'] !=  None:
            if request.method=="POST":
                title = request.POST.get("title")
                description = request.POST.get("description")
                location = request.POST.get("location")
                salary = request.POST.get("salary")
                jobtype = request.POST.get("jobtype")
                lastdate = request.POST.get("lastdate")
                posteddate = datetime.date.today().strftime("%d/%m/%Y")
                ji = JobInfo(title=title, description=description, location=location, salary=salary, jobtype=jobtype, lastdate=lastdate, posteddate=posteddate)
                ji.save()
                messages.success(request,"Job Is Posted")
                return redirect('postjob')
            return render(request,'postjob.html')
    except KeyError:
        messages.error(request,'Please Login')
        return redirect('login')

def postedjob(request):
    try:
        if request.session['adminid'] !=  None:
            ji = JobInfo.objects.all()
            return render(request,'postedjob.html', {"ji":ji})
    except KeyError:
        messages.error(request,'Please Login')
        return redirect('login')


