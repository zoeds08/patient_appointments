from rest_framework import serializers
from rest_framework_mongoengine import serializers as mongoserializers

from .models import Patient, Appointment
from datetime import datetime,date

class PatientSerializer(mongoserializers.DocumentSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

    # def create(self, validated_data):
    #     patient = Patient(
    #         name = validated_data['name'],
    #         birth = datetime.strptime(validated_data['birth'].strftime("%Y-%m-%d"), '%Y-%m-%d').strftime("%Y-%m-%d")
    #     )
    #     patient.save()
    #     return patient

class AppointmentSerializer(mongoserializers.DocumentSerializer):
    # id = serializers.CharField(read_only=False)
    class Meta:
        model = Appointment
        fields = '__all__'
