from django.db import models

class Fcuser(models.Model):
	username = models.CharField(max_length=64, verbose_name='username')
	firstname = models.CharField(max_length=64, verbose_name='firstname')
	lastname = models.CharField(max_length=64, verbose_name='lastname')
	useremail = models.EmailField(max_length=64, verbose_name='email')
	password = models.CharField(max_length=128, verbose_name='password')

	def __str__(self):
		return self.username

	class Meta:
		db_table = 'compass_user'
		verbose_name = 'compass user'
		verbose_name_plural = 'compass users'
	
