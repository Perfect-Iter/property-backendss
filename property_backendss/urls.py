from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("admin/", admin.site.urls),    
    path('users/',include('authentication.urls')),
    path('property/',include('property.urls')),
]
