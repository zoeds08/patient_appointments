from django.contrib import admin
from .models import Patient
from .models import Appointment

admin.site.register(Patient)
admin.site.register(Appointment)
