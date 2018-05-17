from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render
import os
# Create your views here.
class HomeView(TemplateView):
    template_name = "index.html"
    def get(self, request):
        # <view logic>
        # context = {}
        # context["name"] = "Akshat"
        # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # STATIC_ROOT = os.path.join(BASE_DIR, 'static')
        # print(STATIC_ROOT)
        return render(request, self.template_name)

class AboutView(TemplateView):
    template_name = "about.html"
    def get(self, request):
        # <view logic>
        # context = {}
        # context["name"] = "Akshat"
        # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # STATIC_ROOT = os.path.join(BASE_DIR, 'static')
        # print(STATIC_ROOT)
        return render(request, self.template_name)