from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth.decorators import login_required
from blog import views
from .views import ArticleList, ArticleCreate, ArticleUpdate, ArticleDelete

urlpatterns = [
	
	path('articles/', login_required(ArticleList.as_view()), name='article'),

	path('articles/create_article/', login_required(ArticleCreate.as_view()), name='create_article'),

	re_path(r'^article/article_update(?P<pk>\d+)$', login_required(ArticleUpdate.as_view()), name='update_article'),

	re_path(r'^article/article_delete(?P<pk>\d+)$', views.ArticleDelete, name='delete_article'),

	path('article/article_success/', views.msj_article, name='msj_article'),
]