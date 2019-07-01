from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Patient, Physician, Appointment


class PatientSerializer(serializers.ModelSerializer):
	class Meta:
		model = Patient
		fields = ('id', 'first_name', 'last_name', 'height', 'weight')

class PhysicianSerializer(serializers.ModelSerializer):
	class Meta:
		model = Physician
		fields = ('id', 'first_name', 'last_name', 'specialty')

class AppointmentSerializer(serializers.ModelSerializer):
	date = serializers.DateTimeField()
	patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())
	physician = serializers.PrimaryKeyRelatedField(queryset=Physician.objects.all())

	def validate_date(self, value):
		if value.minute % 15 != 0:
			return ValueError("Not every 15 minutes.")
		return value

	class Meta:
		model = Appointment
		fields = ('id', 'date', 'patient', 'physician')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')