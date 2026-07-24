from django.shortcuts import render,redirect
from .models import LoginInfo
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
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
                    return redirect("admindash")
                elif user.usertype == 'jobseeker':
                    messages.success(request, "Welcome job seeker")
                    return redirect("login")
        except LoginInfo.DoesNotExist:
            messages.error(request, "Invalid username or password")
            return redirect("login")
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

