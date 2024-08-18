from django.urls import path
# from append_local.views import test

from member import views
# from django.views.generic import TemplateView # type: ignore

urlpatterns = [
    
    path("register/", views.save_member, name= "save_member"),
    path("edit_data/", views.edit_data, name= "edit_data"),
    path("login/", views.login, name= "login"),
    path("logout/", views.logout, name= "logout"),
    path("data/", views.get_data, name= "get_data"),
    path("all_data/", views.get_all_data, name= "get_all_data"),
    path("verification/", views.verification_email, name= "verification_email"),
    path("verification/<uidb64>/<token>/", views.activate_account, name= "activate_account"),
    
]