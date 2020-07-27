from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from random_app import views
# app_name = "random_app"
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'random_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^airbnb/', include('random_app.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^base', views.shadan, name='base'),
    url(r'^accounts/', include('accounts.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
