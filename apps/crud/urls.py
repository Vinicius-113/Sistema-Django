
from django.urls import path

from . import views


urlpatterns = [

    path('', views.index, name='index'),

    path('novoPaciente/', views.index, name='novo-paciente'),

]

