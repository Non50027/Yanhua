from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from shop import views

product_img= static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

urlpatterns = [
    
    path("save_order/", views.login, name="login"),
    path('product/', views.get_product, name="get_product"),
    
]+ product_img
