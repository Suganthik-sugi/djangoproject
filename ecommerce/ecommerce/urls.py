"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from product import views as v1
from django.db import IntegrityError

urlpatterns = [
    path('',v1.home,name="index"),
    path('admin/', admin.site.urls),
    path('home/',v1.home,name='home'),
    path('result/',v1.result, name="result"),
    path('edit/<int:id>',v1.edit),
    path('update/<int:id>', v1.update,name='update'), 
    path('delete/<int:id>',v1.delete,name='delete'),
    path('forminsert',v1.forminsert,name='forminsert')
]
handlerIntegrityError = 'v1.IntegrityError'