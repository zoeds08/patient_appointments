from rest_framework import serializers
from rest_framework_mongoengine import serializers as mongoserializers

from .models import Patient, Appointment


class AppointmentSerializer(mongoserializers.DocumentSerializer):
    # id = serializers.CharField(read_only=False)
    class Meta:
        model = Appointment
        fields = '__all__'

class PatientSerializer(mongoserializers.DocumentSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
