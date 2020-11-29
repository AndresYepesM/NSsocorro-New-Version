from django import forms
from .models import Article

class DateInput(forms.DateInput):
	input_type = 'date'


class ArticleCreate(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body', 'publication']

        widgets = {'publication': DateInput()}