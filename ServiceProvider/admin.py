from django.contrib import admin
from .models import OperatorProfile,Attendant,OperatorService
# Register your models here.
admin.site.register(OperatorProfile)
admin.site.register(Attendant)
admin.site.register(OperatorService)