from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('logout', user_logout, name='user_logout'),
    path('', user_login , name='user_login'),
    path('home-page', home_page , name='home_page'),
    path('loged-user', loged_user , name='loged_user'),
    path('pbs-info', pbs_info , name='pbs_info'),
    path('change-password', change_password , name='change_password'),

    
    
    
]
