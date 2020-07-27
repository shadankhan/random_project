from django.db import models

# Create your models here.

class Amenities(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Property(models.Model):
	title = models.CharField(max_length=150)
	description = models.TextField()
	images = models.ImageField(upload_to="static/property_image")
	location = models.CharField(max_length=300)
	price_per_day = models.IntegerField()
	amenities = models.ManyToManyField(Amenities)
	available_date = models.DateField()
	pub_date = models.DateTimeField('date published', auto_now_add=True, null=True, blank=True)

	def __unicode__(self):
		return self.title



				
