from django.urls import path
from activity import views
from django.conf import settings
from django.conf.urls.static import static

img= static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)


urlpatterns= [
    
    path("add/", views.add_activity, name= "add_activity"),
    path("photo/", views.add_photo, name= "add_photo"),
    path("get/", views.get_activities, name= "get_activities"),
    path("update/", views.update_activity, name= "update_activity"),
    path("delete/", views.delete_activity, name= "delete_activity"),
    
]+ img