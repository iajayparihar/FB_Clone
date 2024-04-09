from django.contrib import admin

# Register your models here.
from register.models import *


class CustomAdmin(admin.ModelAdmin):
    list_display = ['username','first_name','last_name','password']

admin.site.register(CustomUser,CustomAdmin)