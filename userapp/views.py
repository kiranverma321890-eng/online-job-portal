from django.shortcuts import render,redirect
from django.contrib import messages
from django.views.decorators.cache import cache_control
from mainapp.models import JobSeeker,LoginInfo
from adminapp.models import JobInfo
from . models import Response
import datetime

# Create your views here.
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def userdash(request):
    try:
        if request.session['userid']!=None:
            js=JobSeeker.objects.get(emailaddress=request.session['userid'])
            return render(request,'userdash.html',{"js":js})
    except KeyError:
        messages.error(request,"Login First")
        return redirect('login')

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def userlogout(request):
    try:
        if request.session['userid']!=None:
            del request.session["userid"]
            messages.success(request,"Logged-Out Successfully✅")
            return redirect('login')
    except KeyError:
        messages.error(request,"Login First")
        return redirect('login')
    
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def viewjobs(request):
    try:
        if request.session['userid']!=None:
            js=JobSeeker.objects.get(emailaddress=request.session['userid'])
            ji=JobInfo.objects.all()
            return render(request,'viewjobs.html',{"js":js,"ji":ji})
    except KeyError:
        messages.error(request,"Login First")
        return redirect('login')

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def changeuserpwd(request):
    try:
        if request.session['userid'] !=  None:
            if request.method == "POST":
                oldpassword = request.POST.get("oldpassword")
                newpassword = request.POST.get("newpassword")
                confirmpassword = request.POST.get("confirmpassword")
                if newpassword!=confirmpassword:
                    messages.error(request,"Newpassword and Confirmpassword are not equal")
                    return redirect("changeuserpwd")
                try:
                    obj = LoginInfo.objects.get(username=request.session['userid'],password=oldpassword)
                    LoginInfo.objects.filter(username=request.session['userid']).update(password=newpassword)
                    messages.success(request,"Password is changed successfully✅")
                    return redirect("userlogout")
                except:
                    messages.error(request,"Old Password is Incorrect")
                    return redirect("changeuserpwd")
            return render(request,'changeuserpwd.html')
    except KeyError:
        messages.error(request,'Please Login')
        return redirect('login')

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def giveresponse(request):
    try:
        if request.session['userid']!=None:
            js=JobSeeker.objects.get(emailaddress=request.session['userid'])
            if request.method == "POST":
                responsetype = request.POST.get("responsetype")
                subject = request.POST.get("subject")
                responsetext = request.POST.get("responsetext")
                name = js.name
                contactno = js.contactno
                posteddate = datetime.datetime.today().strftime("%d/%m/%Y")
                res=Response(name=name, contactno=contactno, responsetype=responsetype, subject=subject, responsetext=responsetext, posteddate=posteddate)
                res.save()
                messages.success(request,"Response Submitted Successfully✅")
                return redirect("giveresponse")
            return render(request,'giveresponse.html',{"js":js})
    except KeyError:
        messages.error(request,"Login First")
        return redirect('login')
