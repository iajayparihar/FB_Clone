from django.contrib import admin

# Register your models here.
from .models import UserPost, UserComments

admin.site.register(UserComments)

class UserPostAdmin(admin.ModelAdmin):
    list_display = ['user']
    
admin.site.register(UserPost, UserPostAdmin)
    