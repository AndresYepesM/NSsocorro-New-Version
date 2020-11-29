from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from blog import views
from .views import ArticleList

urlpatterns = [
	
	path('articles/', login_required(ArticleList.as_view()), name='article'),
]