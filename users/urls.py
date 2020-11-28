from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from users import views
from .views import UserEditView

urlpatterns = [

	path('', views.admin_home, name='admin_home'),

	path('singup/', views.signup, name='singup'),

	path('new_user_success/', views.msj_success, name='new_user'),

	path('profile/', login_required(UserEditView.as_view()), name='profile'),

	path('profile_update_success/', views.profile_success, name='profile_update'),

	# Reset Password urls

    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='"password_reset_done'),

	path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),

	path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]