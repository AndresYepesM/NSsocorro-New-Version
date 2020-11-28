from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from readers import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    re_path('administration/', include('users.urls')),
    path('', views.home, name='home')
]
