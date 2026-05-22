from django.contrib import admin
from .models import Location, Job, Jobseeker, Client, Product, Vendor

# Register your models here.
admin.site.register(Jobseeker)
admin.site.register(Job)
admin.site.register(Location)
admin.site.register(Client)
admin.site.register(Vendor)
admin.site.register(Product)