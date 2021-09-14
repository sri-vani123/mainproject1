from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse
from .forms import *

# Create your views here.
def home(request):
    attendance = Attendance.objects.all()
    context = {
        'attendance': attendance,
    }
    return render(request,'schoolapp/home.html', context)

def addAttendance(request):
    if request.user.is_authenticated:
        form=addAttendanceform()
        if(request.method=='POST'):
            form=addAttendanceform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'schoolapp/addAttendance.html',context)
    else:
        return redirect('home')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = createuserform()
        if request.method == 'POST':
            form = createuserform(request.POST)
            if form.is_valid():
                user = form.save()
                return redirect('login')
        context = {
            'form': form,
        }
        return render(request, 'schoolapp/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
       context={}
       return render(request,'schoolapp/login.html',context)

def logoutPage(request):
    logout(request)
    return redirect('/')