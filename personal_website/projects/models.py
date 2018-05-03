from django.db import models
from projects.manager import ProjectManager
# Create your models here.


class Technology(models.Model):
	name = models.CharField(max_length = 40)

	
	def __str__(self):
		return self.name

class Project(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()
	summary = models.TextField()
	technology = models.ManyToManyField(Technology)

	objects = ProjectManager()

	def __str__(self):
		return self.name