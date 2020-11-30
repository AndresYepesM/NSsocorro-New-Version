from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Article(models.Model):

	title = models.CharField(max_length=35, verbose_name='Title')
	body = RichTextField(config_name='default')
	publication = models.DateField(blank=False, verbose_name='publication')
	class Mate:
		ordering = ["id"]
		verbose_name_plural = "Articles"
	def __str__(self):
		return str(self.title)