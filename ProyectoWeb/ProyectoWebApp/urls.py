from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('servicios', views.servicios, name='Servicios'),
    path('tienda', views.Tienda, name='Tienda'),
    path('blog', views.blog, name='blog'),
    path('contacto', views.contacto, name='contacto'),
]
