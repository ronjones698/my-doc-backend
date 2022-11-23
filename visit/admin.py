from django.contrib import admin
from .models import Visit,Consultation,Laboratory,Imaging,Prescription
# Register your models here.
admin.site.register(Visit)
admin.site.register(Consultation)
admin.site.register(Laboratory)
admin.site.register(Imaging)
admin.site.register(Prescription)




