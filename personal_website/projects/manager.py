from django.db import models
# from projects.serializers import ProjectsSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
# from projects.models import Project

class ProjectManager(models.Manager):
	def getAllProjects(self):
		# from projects.models import Project
		projects = self.all()
		# serializer = ProjectsSerializer(instance = projects, many=True)
		# content = JSONRenderer().render(serializer.data)
		
		return projects

	def getProject(self, id = 1):
		try:
			project = self.get(id = id)
		except:
			project = self.get(id = 1)
		return project