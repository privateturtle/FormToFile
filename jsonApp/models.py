# encoding: utf-8

from django.db import models

# Create your models here.
class FModel(models.Model):
	"""Model fuer ein Formular"""
	organame				= models.CharField(max_length=255, blank=True)
	orgaaddition			= models.CharField(max_length=255, blank=True)
	companyadressname		= models.CharField(max_length=255)
	companyadressaddition	= models.CharField(max_length=255, blank=True)
	companyadressstreet		= models.CharField(max_length=255)
	companyadresspobox		= models.PositiveSmallIntegerField(max_length=5)
	companyadresscity		= models.CharField(max_length=255)
	companyadresscountry	= models.CharField(max_length=255)
	companyphone			= models.PositiveIntegerField(max_length=30)
	companyfax				= models.PositiveSmallIntegerField(max_length=30, null=True)
	companyweb				= models.URLField(max_length=255)
	username				= models.CharField(max_length=255)
	usersurname				= models.CharField(max_length=255)
	usermail				= models.EmailField(max_length=255)
	userphone				= models.PositiveSmallIntegerField(max_length=30)
	
	
	class Meta:
		pass
		
	def __unicode__(self):
		return self.name
	
