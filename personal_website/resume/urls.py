from django.conf.urls import include, url
from django.contrib import admin
from views import ResumeView
admin.autodiscover()
# import projects
urlpatterns = [
    # Examples:
    # url(r'^$', 'personal_website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', ResumeView.as_view(), name = 'Resume-Home'),
]
