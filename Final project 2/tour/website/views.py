from django.shortcuts import render,redirect
from.forms import Signupform,Loginform,Vendorform
from django.contrib.auth import authenticate,login,logout
from.models import Listtour,Vendorf

# Create your views here.

def home(request):
    return render(request,'home.html')

def home2(request):
    return render(request,'home2.html')

def signup(request):
    if request.method=='POST':
        form=Signupform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/logins')
    else:
        form=Signupform()
    return render(request,'signup.html',{'form':form})


def logins(request):
    if request.method == 'POST':
        form = Loginform(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']

            user=authenticate(request,username=username,password=password)

            if user:
                login(request,user)
                return redirect('home2')

    else:
        form=Loginform()
    return render(request,'login.html',{'form':form})

def logouts(request):
    logout(request)
    return redirect('logins')

def tours(request):
    return render(request,'tours.html')

def m_tours(request):
    obj=Listtour.objects.all()
    return render(request,'tours.html',{'example':obj})

def edu(request):
    return render(request,'edu.html')

def payup(request):
    return render(request,'payup.html')

def vendor(request):
    if request.method=='POST':
        form=Vendorform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home2')

    else:
        form=Vendorform()
    return render(request,'vendor.html',{'form':form})
