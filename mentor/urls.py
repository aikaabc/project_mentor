from django.urls import path, include
from django.contrib import admin
from . views import api_root

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_root/', api_root),
    path('accounts/', include('accounts.urls')),
]
