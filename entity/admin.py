from django.contrib import admin
from .models import Patient
from .models import Appointment

class PatientAdmin(admin.ModelAdmin):
    list_display = ('name','birth',)

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'dateTime',)

admin.site.register(Patient, PatientAdmin)
admin.site.register(Appointment, AppointmentAdmin)
