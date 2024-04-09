from django.urls import path
from .import views

urlpatterns = [
    path('', views.dairy, name='dairy'),
    path('add', views.add, name='add')
]
