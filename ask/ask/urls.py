from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', include('qa.views.test'),
    url(r'^signup/', include('qa.views.test'),
    url(r'^question/\w+/', include('qa.views.test'),
    url(r'^ask/', include('qa.views.test'),
    url(r'^popular/', include('qa.views.test'),
    url(r'^new/', include('qa.views.test'),
)