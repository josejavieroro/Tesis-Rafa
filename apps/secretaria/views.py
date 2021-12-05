from django.forms.forms import Form
from apps import secretaria
from django.shortcuts import render
from django.http.response import HttpResponseForbidden
from django.views.generic import *
from.models import *
from .forms import *
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from django.urls import reverse_lazy



#Aqui van las vistas


#Esta es listar
class FacultadListView(ListView):
    model = Facultad
    template_name = "facultad/listar.html"

#crear
class FacultadCreateView(CreateView):
    model = Facultad
    template_name = "facultad/crear.html"
    form_class = FacultadForm
    success_url = reverse_lazy('facultad_lista')

#eliminar
class FacultadDeleteView(DeleteView):
    model = Facultad
    template_name = "facultad/eliminar.html"
    form_class = FacultadForm
    success_url = reverse_lazy('facultad_lista')

#actualizar
class FacultadEditView(UpdateView):
    model = Facultad
    template_name = "facultad/actualizar.html"
    form_class = FacultadForm
    success_url = reverse_lazy('facultad_lista')


#para las demas clases del modelo es lo mismo


class MiTemplate(TemplateView):
    template_name = "emrpesa/crear.html"


class EstudianteListView(ListView):
    model = Estudiante
    template_name = "estudiante/listar.html"


class EstudainteCreateView(CreateView):
    model = Estudiante
    template_name = "estudiante/crear.html"


class ProfesorCreateView(CreateView):
    model = Profesor
    template_name = "profesor/crear.html"
