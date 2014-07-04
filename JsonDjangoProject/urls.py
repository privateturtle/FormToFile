from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    
	url(r'^$', 'jsonApp.views.FModel'),
    url(r'^$', 'jsonApp/index.html'),
    url(r'^admin/', include(admin.site.urls)),
)
