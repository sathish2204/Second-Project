"""second_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('select',views.select),
    path('update/<int:score>/<int:overs>/<str:covers>/<str:team1>/<str:team2>/<str:striker>/<str:non_striker>/<str:bowler>/<int:wickets>/<int:pid1>/<int:pid2>/<int:gone>/<int:stbow>/<int:op1b>/<int:op2b>/<int:op1r>/<int:op2r>/<str:b1>/<str:b2>/<str:b3>/<str:b4>/<str:b5>/<str:b6>/<str:sp1>/<str:sp2>/<str:bowo>/<int:bowr>/<int:boww>',views.update,name='update'),
    path('delete',views.delete,name='delete'),
    path('allemployes',views.allemployes),
    path('insert',views.insert),
    path('update2/<int:score>/<int:overs>/<str:covers>/<str:team1>/<str:team2>/<str:striker>/<str:non_striker>/<str:bowler>/<int:wickets>/<int:pid1>/<int:pid2>/<int:gone>/<int:stbow>/<int:op1b>/<int:op2b>/<int:op1r>/<int:op2r>/<str:b1>/<str:b2>/<str:b3>/<str:b4>/<str:b5>/<str:b6>/<str:sp1>/<str:sp2>/<str:bowo>/<int:bowr>/<int:boww>',views.update2,name='update2'),
    path('delete2',views.delete,name='delete2'),
   
    
]
