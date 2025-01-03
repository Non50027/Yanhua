from django.urls import path
from shop import views

urlpatterns= [
    
    path('add/', views.add, name= "add"),
    
]
