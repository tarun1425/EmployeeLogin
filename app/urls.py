from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    
]

'''
    path('loginPage/',views.loginPage,name='loginPage'),
    path('registerPage/',views.registerPage,name='registerPage'),
'''