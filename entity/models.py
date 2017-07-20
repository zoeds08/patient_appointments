from django.db import models
from django.utils import timezone

class Patient(models.Model):
    name = models.ForeignKey('auth.User')
    birth = models.DateField()

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.name)

    # def getAppoints(self):


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    dateTime = models.DateTimeField()

    def publish(self):
        self.save()

    # def my_property(self):
    #     return 'Patient:' + self.patient.name + '; Birth:' + self.patient.birth + '; Appointment Date:' + self.dateTime
    # # my_property.short_description = "Appointment information"


    def __str__(self):
        return str(self.patient)
