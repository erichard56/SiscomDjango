from django.urls import path
from . import views

urlpatterns = [
    path('', views.abonados, name='abonados'),
    path('detalles/<int:id>', views.detalles, name='detalles'),
]
