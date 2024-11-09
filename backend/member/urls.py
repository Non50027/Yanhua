from django.urls import path
from member import views

urlpatterns = [
    
    path("register/", views.save_member, name= "save_member"),
    path("edit_data/", views.edit_data, name= "edit_data"),
    path("login/", views.login, name= "login"),
    path("logout/", views.logout, name= "logout"),
    path("data/", views.get_data, name= "get_data"),
    path("all-data/", views.get_all_data, name= "get-all-data"),
    path("verification/<name>", views.verification_email, name= "verification_email"),
    path("verification/<uidb64>/<token>/", views.activate_account, name= "activate_account"),
    
]