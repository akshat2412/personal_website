from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from projects.models import Project
from rest_framework.response import Response
from serializers import ProjectsSerializer

# Create your views here.
class ProjectsView(TemplateView):
    template_name = "projects.html"

    def get(self, request):
        # <view logic>
        projects_object = Project.objects.getAllProjects()
        serializer = ProjectsSerializer(projects_object, many = True)

        content = {"projects_data": serializer.data}
        
        return render(request, self.template_name, content)


class SingleProjectView(TemplateView):
    template_name = "single-project.html"
    def get(self, request,*args, **kwargs):
        # <view logic>
        project_id = kwargs["project_id"]
        project_id = int(project_id)


        project = Project.objects.getProject(project_id)
        
        serializer = ProjectsSerializer(project)
        content = {"project_data":serializer.data}
        
        return render(request, self.template_name, content)