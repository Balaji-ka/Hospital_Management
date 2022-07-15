from django.db import models

# Create your models here.
class Doctor(models.Model):
    Name=models.CharField(max_length=50)
    Mobile=models.IntegerField()
    Specialist=models.CharField(max_length=50)
    def __str__(self):
        return self.Name

class Patient(models.Model):
    Name=models.CharField(max_length=50)
    Gender=models.CharField(max_length=10)
    Mobile = models.IntegerField()
    Address = models.TextField()
    def __str__(self):
        return self.Name

class Appointment(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField()
    def __str__(self):
        return self.doctor.Name+"__"+self.patient.Name




