from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
class ContactView(TemplateView):
    template_name = "conctact.html"
    def get(self, request):
        # <view logic>
        return render(request, self.template_name)