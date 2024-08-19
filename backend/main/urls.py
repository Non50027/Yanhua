from django.contrib import admin
from django.urls import path, include
import member.urls, shop.urls, activity.urls, options.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('member/', include(member.urls)),
    path('shop/', include(shop.urls)),
    path('activity/', include(activity.urls)),
    path('options/', include(options.urls)),
    
]
