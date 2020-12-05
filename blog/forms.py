from django import forms
from .models import Article, Activity

class DateInput(forms.DateInput):
	input_type='date'


class NewArticle(forms.ModelForm):
    class Meta:
        model=Article
        widgets={'publication': DateInput()}
        fields=['title','publication', 'body']


class NewActivities(forms.ModelForm):
	class Meta:
		model = Activity
		widgets={'st_date': DateInput(), 'ed_date': DateInput()}
		fields=['st_date','ed_date', 'text']
