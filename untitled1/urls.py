"""untitled1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.urls import path
from apps.secretaria.views import *

urlpatterns = [


    path('admin/', admin.site.urls),


    #Aqui van los urls es copiar y pergar pero le tienes que poner el nombre de las vistas que hagas
    path("facultad_list/",login_required(FacultadListView.as_view()),name="facultad_lista"),
    path("facultad_crear/",login_required(FacultadCreateView.as_view()),name="facultad_crear"),
    path("facultad_eliminar/<int:pk>/",login_required(FacultadDeleteView.as_view()),name="facultad_eliminar"),
    path("facultad_actualizar/<int:pk>/",login_required(FacultadEditView.as_view()),name="facultad_actualizar"),



]




















