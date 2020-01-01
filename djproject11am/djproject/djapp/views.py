from django.shortcuts import render,redirect
from djapp.forms import RegistrationForm,LoginForm
from django.http.response import HttpResponse
from djapp.models import RegistrationData

def registration_view(request):
    if request.method == "POST":
        rform = RegistrationForm(request.POST)
        if rform.is_valid():
            fname = request.POST.get('first_name')
            lname = request.POST.get('last_name')
            uname = request.POST.get('user_name')
            pwd = request.POST.get('password')
            mobile = request.POST.get('mobile')
            email = request.POST.get('email')
            data = RegistrationData(
                first_name=fname,
                last_name=lname,
                user_name=uname,
                password=pwd,
                mobile=mobile,
                email=email
            )
            data.save()
            rform = RegistrationForm()
            return render(request, 'reg.html', {'xyz': rform})
        else:
            return HttpResponse('USer Invalid Data')
    else:
        rform = RegistrationForm()
        return render(request,'reg.html',{'xyz':rform})

def Login_View(request):
    if request.method =="POST":
        lform = LoginForm(request.POST)
        if lform.is_valid():
            uname = request.POST.get('user_name')
            pwd = request.POST.get('password')

            user = RegistrationData.objects.filter(user_name=uname)
            password = RegistrationData.objects.filter(password=pwd)

            if user and password:
                return redirect('/home/')
                # return HttpResponse("Success")
            else:
                return HttpResponse("Fail")
        else:
            return HttpResponse('User Invalid Data')
    else:
        lform = LoginForm()
        return render(request,'logindata.html',{'lform':lform})


def home_view(request):
    return render(request,'project_home.html')


def contact_view(request):
    return render(request,'project_contact.html')


def services_view(request):
    return render(request,'project_services.html')