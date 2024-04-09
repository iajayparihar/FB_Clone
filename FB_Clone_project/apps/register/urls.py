
from django.urls import path
from .views import *
urlpatterns = [
    path('', login_user, name= 'login_user'),
    # path('register/', register_user, name= 'register_user'),
    # path('dashbord/', dashboard, name='dashbord123'),
    path('user_form/', UserForm, name='user_form'),
    path('logout_user/', logout_user, name='logout_user'),
]
