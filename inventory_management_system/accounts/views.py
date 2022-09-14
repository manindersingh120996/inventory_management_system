from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User

# Create your views here.


def login_page(request):
    return render(request,'accounts/login.html')


def loginpage(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['passowrd2']

        myuser = User.objects.create_user(username,email,password1)
        myuser.save()
        massages.success(request, "Your Account Successfully created.")
        
    else:
        return HttpResponse('404 - Not Found')
    context = {}
    return render(request,'accounts/login1.html',context)


def registerpage(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['passowrd2']

        myuser = User.objects.create_user(username,email,password1)
        myuser.save()
        massages.success(request, "Your Account Successfully created.")
        
    else:
        return HttpResponse('404 - Not Found')
        
    context = {}
    return render(request,'accounts/login1.html',context)
    context = {}
    return render(request,'accounts/register.html',context)