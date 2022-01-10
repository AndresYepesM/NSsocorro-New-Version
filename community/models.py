from django.db import models
from PIL import Image

# Create your models here.


class MembersProfile(models.Model):

	name = models.CharField(max_length=60, verbose_name='Name and last name')
	bio = models.TextField()
	photo = models.ImageField(upload_to='static/img/upload/members', blank=True)
	class Meta:
		ordering = ["-id"]
		verbose_name_plural = "Members Profile"
	def __str__(self):
		return str(self.name)


class CommunityProfiles(models.Model):

	name = models.CharField(max_length=60, verbose_name='name of the community')
	bio = models.TextField()
	photo = models.ImageField(upload_to='static/img/upload/community', blank=True)
	class Meta:
		ordering =["-id"]
		verbose_name_plural = "Community Profiles"
	def __str__(self):
		return str(self.name)