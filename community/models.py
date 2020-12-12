from django.db import models

# Create your models here.


class MembersProfile(models.Model):

	name = models.CharField(max_length=60, verbose_name='Name and last name')
	bio = models.TextField()
	img = models.ImageField(upload_to='static/img/upload/members')
	class Meta:
		ordering = ["-id"]
		verbose_name_plural = "Members Profile"
	def __str__(self):
		return str(self.name)