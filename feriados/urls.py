from django.urls import path
from . import views

urlpatterns = [
    path('', views.feriados, name='feriados'),
]
