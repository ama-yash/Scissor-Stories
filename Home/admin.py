from django.contrib import admin
from .models import City,State,Service,Offer,Role
# Register your models here.
admin.site.register(City)
admin.site.register(State)
admin.site.register(Service)
admin.site.register(Offer)
admin.site.register(Role)