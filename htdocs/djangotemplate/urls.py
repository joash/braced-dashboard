from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangotemplate.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #base template include
    url(r'^$', TemplateView.as_view(template_name='base.html')),

    #admin
    url(r'^admin/', include(admin.site.urls)),

    #home
    url(r'^home', 'views.home', name='home'),
    url(r'^contact', 'views.contact', name='contact'),
    url(r'^faq', 'views.faq', name='faq'),
    url(r'^documentation', 'views.documentation', name='documentation'),

    #local login
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
)
