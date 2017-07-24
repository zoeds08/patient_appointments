from __future__ import unicode_literals

from django.template.response import TemplateResponse

from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet
# from rest_framework.permissions import IsAuthenticated

from .serializers import *
from .models import Patient, Appointment

from rest_framework import generics

class ApppointmentViewSet(MongoModelViewSet):
    """
    Contains information about inputs/outputs of a single program
    that may be used in Universe workflows.
    """
    # lookup_field = 'id'
    serializer_class = AppointmentSerializer
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        return Appointment.objects.all()

class PatientViewSet(MongoModelViewSet):
    # lookup_field = 'id'
    serializer_class = PatientSerializer

    def get_queryset(self):
        return Patient.objects.all()


class PatientAppointmentsList(generics.ListAPIView):
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        return Appointment.objects.filter(patient=self.kwargs['patient'])


from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse

def index_view(request):
    context = {}
    return TemplateResponse(request,'entity/home.html',context)

def patient_list(request):
    patients = Patient.objects.all();
    return TemplateResponse(request, 'entity/patient_list.html', {'patients':patients})

def appointment_list(request):
    appointments = Appointment.objects.all();
    return TemplateResponse(request, 'entity/appointment_list.html', {'appointments':appointments})

def patient_appointment_list(request, pk):
    appointments = Appointment.objects.filter(patient=pk)
    return TemplateResponse(request, 'entity/patient_appointment_list.html', {'appointments':appointments})

def patient_edit(request):
        # patient = get_object_or_404(Patient, pk=pk)
        serializer = PatientSerializer(data=request)
        if not serializer.is_valid():
            return HttpResponse("bad request")
        serializer.save()
        return TemplateResponse(request, 'entity/patient_edit.html', {'serializer':serializer})
        # Response(serializer.data,template_name='entity/patient_edit.html', status=status.HTTP_201_CREATED)

def appointment_edit(request):
        # appointment = get_object_or_404(Appointment, pk=pk)
        serializer = AppointmentSerializer
        # if not serializer.is_valid():
        #     return Response({'serializer': serializer, 'appointment': appointment})
        # serializer.save()
        return TemplateResponse(request, 'entity/appointment_edit.html', {'serializer':serializer})
