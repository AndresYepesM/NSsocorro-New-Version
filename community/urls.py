from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from .views import MembersList
from community import views

urlpatterns = [
	path('members/', login_required(MembersList.as_view()), name='members'),

	path('members/search', views.SearchMenmers, name="SearchBar"),

	path('members/result', views.SearchForm, name="SearchBarForm"),
	
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)