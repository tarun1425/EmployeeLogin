from django.contrib import admin
from accounts.models import Registration
# Register your models here.

class NameAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','username','email')
    
admin.site.register(Registration, NameAdmin)
