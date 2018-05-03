from django.conf.urls import include, url
from django.contrib import admin
from views import HomeView

urlpatterns = [
    # Examples:
    # url(r'^$', 'personal_website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomeView.as_view(), name = 'Home'),
    url(r'^projects/', include('projects.urls')),
    url(r'^resume/', include('resume.urls')),
    url(r'^contact/', include('contact.urls')),
]
