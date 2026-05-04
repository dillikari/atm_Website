"""
URL configuration for projectdatabaseATM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from appATM.views import functionOne,functionTwo,functionThree,functionFour,functionFive,functionSix,functionSeven

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',functionOne,name='index'),
    path('accountcreate/',functionTwo,name='accountcre'),
    path('deleteaccount/',functionThree,name='delete'),
    path('widthdrawal/',functionFour,name='widthdraw'),
    path('deposite/',functionFive,name='depositeamt'),
    path('searchaccount/',functionSix,name='search'),
    path('listofcustomer/',functionSeven,name='customerlist')
]
