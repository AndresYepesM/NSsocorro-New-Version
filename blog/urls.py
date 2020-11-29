from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from blog import views
from .views import ArticleList, ArticleCreate

urlpatterns = [
	
	path('articles/', login_required(ArticleList.as_view()), name='article'),

	path('articles/create_article/', login_required(ArticleCreate.as_view()), name='create_article'),

	path('article/article_success/', views.msj_article, name='msj_article'),
]