from django import forms
from PIL import ImageFilter
from .models import *



class CreateMember(forms.ModelForm):
	class Meta:

		model = MembersProfile
		fields=[
			'name',
			'bio',
			'photo',
		]
		labels = {
			'name': 'Name and last name',
			'bio': 'Biography',
			'photo': 'Picture or profile photo',
		}