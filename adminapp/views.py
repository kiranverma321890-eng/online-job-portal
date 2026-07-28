from django.shortcuts import render,redirect
from django.contrib import messages
from mainapp.models import JobSeeker, LoginInfo, Enquiry
from . models import JobInfo
import datetime
from django.views.decorators.cache import cache_control
from userapp.models import Response

# Create your views here.
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def admindash(request):
    try:
        if request.session['adminid'] !=  None:
            total_jobs = JobInfo.objects.count()
            total_seekers = JobSeeker.objects.count()
            total_postedjob = JobSeeker.objects.count()
            total_enquiry =Enquiry.objects.count()
            return render(request,'admindash.html',
                {
                 "total_jobs" :total_jobs,
                 "total_seekers" :total_seekers,
                 "total_postedjob" :total_postedjob,
                 "total_enquiry" :total_enquiry 
                })
    except KeyError:
        messages.error(request,'Please Login')
        return redirect('login')

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def adminlogout(request):
    try:
        if request.session['adminid'] != None:
            del request.session['adminid']
            messages.error(request,"You have logged-out successfully")
            return redirect('login')
    except KeyError:
        messages.error(request,'Please Login')
        return redirect('login')

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def jobseeker(request):
    try:
        if request.session['adminid'] !=  None:
            js = JobSeeker.objects.all()
            return render(request,'jobseeker.html', {"js":js})
    except KeyError:
        messages.error(request,'Please Login')
        return redirect('login')

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
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

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def postedjob(request):
    try:
        if request.session['adminid'] !=  None:
            ji = JobInfo.objects.all()
            return render(request,'postedjob.html', {"ji":ji})
    except KeyError:
        messages.error(request,'Please Login')
        return redirect('login')

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def enquiries(request):
    try:
        if request.session['adminid'] !=  None:
            enq=Enquiry.objects.all()
            return render(request,'enquiries.html',{"enq":enq})
    except KeyError:
        messages.error(request,'Please Login')
        return redirect('login')

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def changeadminpwd(request):
    try:
        if request.session['adminid'] !=  None:
            if request.method == "POST":
                oldpassword = request.POST.get("oldpassword")
                newpassword = request.POST.get("newpassword")
                confirmpassword = request.POST.get("confirmpassword")
                if newpassword!=confirmpassword:
                    messages.error(request,"Newpassword and Confirmpassword are not equal")
                    return redirect("changeadminpwd")
                try:
                    LoginInfo.objects.get(username=request.session['adminid'],password=oldpassword)
                    LoginInfo.objects.filter(username=request.session['adminid']).update(password=newpassword)
                    messages.success(request,"Password is changed successfully")
                    return redirect("adminlogout")
                except LoginInfo.DoesNotExist:
                    messages.error(request,"Old Password is Incorrect")
                    return redirect("changeadminpwd")
            return render(request,'changeadminpwd.html')
    except KeyError:
        messages.error(request,'Please Login')
        return redirect('login')

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def viewfeedback(request):
    try:
        
        if request.session['adminid'] !=  None:
            res =Response.objects.filter(responsetype="feed")
            return render(request,'viewfeedback.html',{"res":res})
    except KeyError:
        messages.error(request,'Please Login')
        return redirect('login')


@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def viewcomplaint(request):
    try:
        
        if request.session['adminid'] !=  None:
            res =Response.objects.filter(responsetype="comp")
            return render(request,'viewcomplaint.html',{"res":res})
    except KeyError:
        messages.error(request,'Please Login')
        return redirect('login')

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def deleteenq(request,id):
    try:
        if request.session['adminid'] !=  None:
            enq = Enquiry.objects.get(id=id)
            enq.delete()
            messages.success(request,"Enquiry is deleted Successfully✅")
            return render(request,'admindash.html')
    except KeyError:
        messages.error(request,'Please Login')
        return redirect('login')
