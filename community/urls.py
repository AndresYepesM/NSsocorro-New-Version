from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth.decorators import login_required
from .views import MembersProfile

urlpatterns = [
	path('members/', login_required(MembersProfile.as_view()), name='members')
]