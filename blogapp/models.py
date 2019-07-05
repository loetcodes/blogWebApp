from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class BlogPost(models.Model):
	"""
	Post object for each post
	"""
	title = models.CharField(max_length = 200)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)		
	date_created = models.DateTimeField(default = timezone.now)
	date_published = models.DateTimeField(blank = True, null = True)
	text = models.TextField()

	def __str__(self):
		return self.title

	def publish_post(self):
		self.date_published = timezone.now()
		self.save()