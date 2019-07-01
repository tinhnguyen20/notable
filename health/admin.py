from django.contrib import admin

# Register your models here.
from .models import Patient, Physician, Appointment

admin.site.register(Appointment)
admin.site.register(Patient)
admin.site.register(Physician)
