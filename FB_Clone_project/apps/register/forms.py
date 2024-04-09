from django import forms
from register.models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class CustomUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        # fields = '__all__'
        fields = ["username",'first_name','last_name',\
            'email','mobile','age','DOB',\
                'gender']
        widgets = {
            'DOB': forms.DateInput(attrs={'type': 'date'},),
            }
        
        labels = {'email':'Email'}
        