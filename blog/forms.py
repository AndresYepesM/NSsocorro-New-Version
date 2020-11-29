from django import forms
from .models import Article

class DateInput(forms.DateInput):
	input_type='date'


class NewArticle(forms.ModelForm):
    class Meta:
        model=Article
        widgets={'publication': DateInput()}
        fields=['title','publication', 'body']