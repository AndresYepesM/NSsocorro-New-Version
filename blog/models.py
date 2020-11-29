from django.db import models

# Create your models here.


class Article(models.Model):

	title = models.CharField(max_length= 35, verbose_name='Title')
	body = models.TextField(verbose_name = 'Body Article')
	date = models.DateField(blank = False, verbose_name = 'publication date')
	class Mate:
		ordering = ["-id"]
		verbose_name_plural = "Articles"
	def __str__(self):
		return str(self.title)