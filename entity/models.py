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

    def __str__(self):
        return str(self.patient)
