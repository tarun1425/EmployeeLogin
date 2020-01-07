from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from accounts.models import Registration
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def logIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username= username, password= password)
        login(request,user)
        print('login successfully ')
        return redirect('/')
    else:
        return render(request,'accounts/login.html')



def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['first_name']
        
        #create user object
        user = User.objects.create_user(username= username, password=password1, email=email, first_name= first_name, last_name= last_name)
        
        # registration table object
        registration = Registration(username= username, password=password1, email=email, first_name= first_name, last_name= last_name)
        
        # save data of user model
        user.save()
        
        #save data of registration model
        registration.save()
        
        # print for console
        print('user created')
        return redirect('register')
        
    else:
        return render(request,'accounts/register.html')


def logOut(request):
    auth.logout(request)
    return redirect('/')