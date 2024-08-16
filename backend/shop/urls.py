from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from shop import views

img= static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

urlpatterns= [
    
    path("order/create/", views.create_order, name= "create_order"),
    path('order/get/', views.get_order, name= "get_order"),
    path('order/update/', views.update_order, name= "update_order"),
    path('order/delete/', views.delete_order, name= "delete_order"),
    path('product/add/', views.add_product, name= "add_product"),
    path('product/all/', views.get_all_product, name= "get_all_product"),
    path('product/edit/', views.edit_product, name= "edit_product"),
    path('product/delete/', views.delete_product, name= "delete_product"),
    
]+ img
