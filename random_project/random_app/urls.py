from django.conf.urls import patterns, include, url
from random_app import views

urlpatterns=[

	url(r'^$', views.shadan, name="index"),
	url(r'^details_property/(?P<property_id>\d+)/$', views.details_property, name="details_property"),


]