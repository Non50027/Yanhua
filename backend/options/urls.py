from django.urls import path
from options import views
from django.conf import settings
from django.conf.urls.static import static

img= static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)


urlpatterns= [
    
    path("get/", views.get_data, name= "get_data"),
    path("set/", views.save_data, name= "save_data"),
    
]+ img