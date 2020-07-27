from django.conf.urls import patterns, include, url
from accounts import views

urlpatterns=[

	url(r'^register', views.register, name="register"),	
	url(r'^login', views.login, name="login"),	
	url(r'^logout', views.logout, name="logout"),



]