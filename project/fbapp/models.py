from django.db import models

class FbModel(models.Model):
	name = models.CharField(max_length=20)
	number = models.IntegerField(unique=True)
	feedback = models.CharField(max_length=400)

	def __str__(self):
		return self.name