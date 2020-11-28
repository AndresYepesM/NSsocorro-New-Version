from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistroForm(UserCreationForm):

	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
			'is_staff'
		]
		labels = {
			'username': 'Username',
			'first_name': 'First name',
			'last_name': 'Last name',
			'staff status':'Staff Status',
			'email': 'Email',
		}


class ProfileUpdate(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']