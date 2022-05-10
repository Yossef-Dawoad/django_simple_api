from django.urls import path
from sympy import viete
from . import views

urlpatterns = [
    path('states', views.listall_states, name='states'),
    path('last-state/', views.read_state, name='last-state'),
    path('create-state/', views.create_state, name='create-state'),
]