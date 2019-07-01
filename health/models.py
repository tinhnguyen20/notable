from django.db import models
from django.utils.timezone import now
from datetime import datetime, timedelta


# Create your models here.
class Patient(models.Model):
	first_name = models.CharField(max_length=64)
	last_name = models.CharField(max_length=64)

	height = models.FloatField()
	weight = models.FloatField()

	class Meta:
		ordering = ('first_name',)

class Physician(models.Model):
	SPECIALTY_CHOICES = [(str(i), j) for i, j in enumerate(['OBGYN', 'PT', 'ER', 'FM'])]

	first_name = models.CharField(max_length=64)
	last_name = models.CharField(max_length=64)
	specialty = models.CharField(max_length=16, choices=SPECIALTY_CHOICES, default='FM')

	class Meta:
		ordering = ('last_name',)

class Appointment(models.Model):
	KIND_CHOICES = [("0", "New Patient"), ("1", "Follow Up")]

	date = models.DateTimeField()
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	physician = models.ForeignKey(Physician, on_delete=models.CASCADE)
	notes = models.TextField(default="")
	kind = models.CharField(max_length=16, choices=KIND_CHOICES)
	created_time = models.DateTimeField(auto_now=True)

	def appointment_by_doctor(doctor_id):
		return Appointment.objects.get(physician=doctor_id)

	def appointment_by_doctor_by_day(doctor_id, date):
		# string of form MM/DD/YYYY
		end_date = date + timedelta(days=1)
		return appointment_by_doctor(doctor_id).filter(date__range=[date, end_date])


	class Meta:
		ordering = ('date',)

