from django.urls import path
from . import views

urlpatterns = [
    path('', views.vehiculos, name='vehiculos'),
]
