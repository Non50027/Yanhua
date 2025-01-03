from django.contrib import admin
from django.urls import path, include
import member.urls, shop.urls, activity.urls, options.urls, order.urls, admin.urls

urlpatterns = [
    path('member/', include(member.urls)),
    path('shop/', include(shop.urls)),
    path('order/', include(order.urls)),
    path('activity/', include(activity.urls)),
    path('options/', include(options.urls)),
    path('admin/', include(admin.urls)),
    
]
