from django.shortcuts import render, redirect, HttpResponseRedirect,reverse

# Create your views here.
from register.models import CustomUser
from register.forms import CustomUserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
# register user


def UserForm(request):
    if request.method != 'POST':
        form = CustomUserForm()
        return render(request, 'register/user_form.html', {'form': form})

    username = CustomUser.objects.filter(username=request.POST.get('username'))
    if username:
        # username already exists
        form = CustomUserForm()
        return render(request, 'register/user_form.html', {'form': form, 'msg': 'username already exist'})

    form = CustomUserForm(request.POST)
    if form.is_valid():
        form.save()
        # messages.success(request,'Account Created Succesfully!!!')
        return redirect('/')

    return render(request, 'register/user_form.html', {'form': form})


def login_user(request):
    if request.method != 'POST':
        fm = AuthenticationForm()
        return render(request, 'register/login.html', {"form": fm})

    fm = AuthenticationForm(request=request, data=request.POST)
    if fm.is_valid():
        username = fm.cleaned_data.get('username')
        password = fm.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('Post:dashbord')
    else:
        fm = AuthenticationForm()
    return render(request, 'register/login.html', {"form": fm,'context':'check your password or username.'})



def logout_user(request):
    logout(request)
    return redirect('/')



