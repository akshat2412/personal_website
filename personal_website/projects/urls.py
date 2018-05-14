from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import ProjectsView, SingleProjectView
# admin.autodiscover()
# import projects
urlpatterns = [
    # Examples:
    # url(r'^$', 'personal_website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url('^$', ProjectsView.as_view(), name = 'Home'),
    url("^(?P<project_id>[0-9]*)/$", SingleProjectView.as_view(), name = 'Single-Project-Home'),
]
