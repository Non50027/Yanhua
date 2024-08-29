from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from shop import views

img= static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

urlpatterns= [
    
    path('add/', views.add, name= "add"),
    path('get/', views.get, name= "get"),
    path('edit/', views.edit, name= "edit"),
    path('delete/', views.delete, name= "delete"),
    
]+ img
