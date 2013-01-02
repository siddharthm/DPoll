from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
	
urlpatterns = patterns('polls.views',
    url(r'^polls/',include('polls.urls')),
	url(r'^polls/admin/', include(admin.site.urls)),    
)


