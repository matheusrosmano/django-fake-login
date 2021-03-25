from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('controle/', admin.site.urls),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
]
