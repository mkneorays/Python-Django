Create urls.py at application level insted of application level, after that include in project  level urls.py
-----------------------------------------------------
1 > First of all create the project using below command
C:\Users\CHOTKA\Desktop\CorePython\DjangoApps\SingleAppWithMultipleView>django-manage startproject SingleAppWithMultipleViews
2 > Start Application
C:\Users\CHOTKA\Desktop\CorePython\DjangoApps\SingleAppWithMultipleView>python manage.py startapp testapp
3 > Add application to the project inside settings.py
4 > defined view function inside views.py
5 > define url pattern for view function inside urls.py
6 > run server and send request
--------------------------------------------------------------------------
views.py   of testapp
---------------------
from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def date_time_view(request):
    date=datetime.datetime.now()
    s='<h2> The current Date and Time at server is :'+str(date)+'</h2>'
    return HttpResponse(s)

def good_mor_view(request):
    return HttpResponse('<h1>Good Morning Dear....!!!!</h1>')

def good_eve_view(request):
    s='<h2>Good Evening Bor......!!!!!</h2>'
    return HttpResponse(s)

def good_night_view(request):
    return HttpResponse('<h2>Good Night Sweat Dreams.......!!!!</h2>')
  ----------------------------------------------------------------------------------------
# create one file manually inside testapp which name is urls.py
urls.py  of testap
------------------
from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('date/', views.date_time_view, name='date_time_view'),
    path('mor/', views.good_mor_view),
    path('eve/', views.good_eve_view),
    path('night/', views.good_night_view),
]
----------------------------------------------------
# add  urls.py file inside at project level's url.py
urls.py of project level
---------------------------
"""SecondDjangoApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
from testapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('testapp/', include('testapp.urls')),       #   be carefull for this statement
    
]
--------------------------------------------------------------
