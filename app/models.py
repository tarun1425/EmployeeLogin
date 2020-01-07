from django.db import models

# Create your models here.
class EmployeModel(models.Model):
    userFirstName = models.CharField(max_length=25, default='')
    userLastName = models.CharField(max_length=25, default='')
    username = models.CharField(max_length=20, default='')
    
    userCity = models.CharField(max_length=25, default='')
    user_State = (
        ('mp', 'MP'),
        ('up', 'UP'),
        ('dehli', 'DEHLI'),
        ('goa', 'GOA'),
    )
    userState = models.CharField(max_length=5, choices=user_State, default='')
    userPasswsord = models.CharField(max_length=15, default='')
    
    userJoiningCompleted = models.BooleanField(default=False)
    userAddedDate = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.userFirstName}-{self.userLastName}'
    
    