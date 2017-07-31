from mongoengine import Document, fields

class Patient(Document):
    name = fields.StringField(required=True)
    birth = fields.StringField(required=True)

class Appointment(Document):
    patient = fields.ReferenceField(Patient,dbref=True)
    date = fields.DateTimeField(required=True)
