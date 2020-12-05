from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from readers import views
from readers.views import Article


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    re_path('administration/', include('users.urls')),
    re_path('administration/blog/', include('blog.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', views.home, name='home'),

    path('articles/', Article.as_view(), name='article_readers'),
]
