from django.views.generic import TemplateView
from django.http import HttpResponse
# Create your views here.
class ResumeView(TemplateView):
    # template_name = "about.html"
    def get(self, request):
        # <view logic>
        return HttpResponse('This is the Resume page')