from django.urls import path
# from append_local.views import test

from member import views
# from django.views.generic import TemplateView # type: ignore

urlpatterns = [
    
    path("register/", views.register, name="register"),
    path("edit_data/", views.edit_data, name="edit_data"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("data/", views.get_data, name="get_data"),
    path("hello/", views.hello_world, name="hello_world"),
    
]