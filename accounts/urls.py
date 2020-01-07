from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.logIn,name='login'),
    path('logout/',views.logOut,name='logout'),
]

'''
    path('loginPage/',views.loginPage,name='loginPage'),
    path('registerPage/',views.registerPage,name='registerPage'),
'''

# hello bc