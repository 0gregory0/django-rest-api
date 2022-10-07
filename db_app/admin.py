from django.contrib import admin
from .models import Users, Company, Address, Geo

# Register your models here.
admin.site.register(Users)
admin.site.register(Company)
admin.site.register(Address)
admin.site.register(Geo)