from django.shortcuts import render
from django.http import HttpResponse
from random_app.models import Amenities, Property
from django.contrib.auth.models import User, auth

def index(request):
	p = Property.objects.all().order_by('-pub_date')
	query = request.GET.get("q")
	if query:
		latest_property = latest_property.filter(location__icontains=query) | latest_property.filter(title__icontains=query)
	return render(request, 'index.html' ,{'latest_property': latest_property})

def details_property(request, property_id):
	prop = Property.objects.all()
	try:
		prop = Property.objects.get(pk=property_id)
	except:
		print("error")

	return render(request, 'details_property.html', {'prop':prop})

def shadan(request):
	return render(request, 'base.html')

# Create your views here.
