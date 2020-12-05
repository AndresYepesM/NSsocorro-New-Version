from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Article(models.Model):

	title = models.CharField(max_length=35, verbose_name='Title')
	body = RichTextField(config_name='default')
	publication = models.DateField(blank=False, verbose_name='publication')
	class Meta:
		ordering = ["-id"]
		verbose_name_plural = "Articles"
	def __str__(self):
		return str(self.title)


class Activity(models.Model):

	st_date = models.DateField(blank=False, verbose_name='begin of the  activity')
	ed_date = models.DateField(blank=False, verbose_name='end of the  activity')
	text = RichTextField(config_name='default')
	class Meta:
		ordering = ["-id"]
		verbose_name_plural = "Activity"
	def __date__(self):
		return date(self.st_date, self.ed_date)