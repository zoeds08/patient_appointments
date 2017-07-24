from mongoengine import Document, fields

class Patient(Document):
    name = fields.StringField(required=True)
    birth = fields.StringField(required=True)

    # def publish(self):
    #     self.save()
    #
    # def __str__(self):
    #     return str(self.name)



class Appointment(Document):
    patient = fields.ReferenceField(Patient,dbref=True)
    date = fields.StringField(required=True)
    # choices=[('2014,2015,2016,2017'),('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'),('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31')]
    time = fields.StringField(required=True)
    #
    # def publish(self):
    #     self.save()
    #
    # # def my_property(self):
    # #     return 'Patient:' + self.patient.name + '; Birth:' + self.patient.birth + '; Appointment Date:' + self.dateTime
    # # # my_property.short_description = "Appointment information"
    #
    #
    # def __str__(self):
    #     return str(self.patient)
