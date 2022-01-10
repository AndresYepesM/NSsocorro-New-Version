from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from .views import MembersList, NewMember,MembersDone, UpdateMember,MembersDeleteDone
from community import views

urlpatterns = [
	path('members/', login_required(MembersList.as_view()), name='members'),

	path('members/New/', login_required(NewMember.as_view()), name='AddMembers'),

	re_path(r'^members/members_update(?P<pk>\d+)$', login_required(UpdateMember.as_view()), name='UpdateMember'),

	re_path(r'^article/article_delete(?P<pk>\d+)$', views.MemberDelete, name='MemberDelete'),

	path('members/Done/', login_required(MembersDone.as_view()), name='MembersDone'),

	re_path('members/Delete/Done/', login_required(MembersDeleteDone.as_view()), name='MembersDeleteDone'),

	path('members/search', views.SearchMenmers, name="SearchBar"),

	path('members/result', views.SearchForm, name="SearchBarForm"),
	
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)