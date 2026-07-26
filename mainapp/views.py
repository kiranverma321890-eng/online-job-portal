from django.shortcuts import render,redirect
from .models import LoginInfo, JobSeeker, Enquiry
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        contactno = request.POST.get("contactno")
        emailaddress = request.POST.get("emailaddress")
        enquirytext = request.POST.get("enquirytext")
        
    return render(request,'contact.html')

def faq(request):
    return render(request,'faq.html')

def jobs(request):
    return render(request,'jobs.html')

def login(request):
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = LoginInfo.objects.get(username=username,password=password)
            if user is not None:
                if user.usertype == 'admin':
                    messages.success(request, "welcome Admin")
                    request.session['adminid'] =user.username
                    return redirect("admindash")
                elif user.usertype == 'jobseeker':
                    messages.success(request, "Welcome job seeker")
                    return redirect("login")
        except LoginInfo.DoesNotExist:
            messages.error(request, "Invalid username or password")
            return redirect("login")
    return render(request,'login.html')

def register(request):
    if request.method=="POST":
        name = request.POST.get("name")
        gender = request.POST.get("gender")
        contactno = request.POST.get("contactno")
        emailaddress = request.POST.get("emailaddress")
        qualification = request.POST.get("qualification")
        experience = request.POST.get("experience")
        keyskill = request.POST.get("keyskill")
        address = request.POST.get("address")
        password = request.POST.get("password")
        js = JobSeeker(name=name,gender=gender,contactno=contactno,emailaddress=emailaddress,qualification=qualification,experience=experience,keyskill=keyskill,address=address,)
        li = LoginInfo(usertype = 'jobseeker', username = emailaddress, password = password)
        js.save()
        li.save()
        messages.success(request, "Registration done")
        return redirect("register")
        
    return render(request,'register.html')

