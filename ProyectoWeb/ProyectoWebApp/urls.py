from django.urls import path

from ProyectoWebApp import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('servicios/', views.servicios, name='Servicios'),
    path('tienda/', views.Tienda, name='Tienda'),
    path('blog/', views.blog, name='Blog'),
    path('contacto/', views.contacto, name='Contacto'),
]
