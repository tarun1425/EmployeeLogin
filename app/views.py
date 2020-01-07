from django.shortcuts import render
from django.http import HttpResponse
from .models import EmployeModel
# Create your views here.

def index(request):
    return render(request,'app/index.html')




'''def loginPage(request):
    return render(request,'app/account/login.html')

def registerPage(request):
    return render(request,'app/account/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST.get['password']
        '''