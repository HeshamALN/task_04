from django.db import models

# Create your models here.
class Restaurant(models.Model):
	name = models.CharField(max_length=105)
	description = models.TextField()
	# opening_time = models.Charfield(max_length=105)
	# closing_time = models.Charfield(max_length=105)
	opening_time = models.TimeField(auto_now=False, auto_now_add=False)
	closing_time = models.TimeField(auto_now=False, auto_now_add=False)