from django.contrib import admin
from django.urls import path, include
import member.urls, shop.urls, activity.urls, options.urls, order.urls

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/member/', include(member.urls)),
    path('api/shop/', include(shop.urls)),
    path('api/order/', include(order.urls)),
    path('api/activity/', include(activity.urls)),
    path('api/options/', include(options.urls)),
    
]
