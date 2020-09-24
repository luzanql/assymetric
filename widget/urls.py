from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nonce', views.nonce, name='nonce'),
    path('keys', views.generateKeys, name='keys'),
]