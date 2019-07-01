from django.http import HttpResponse, JsonResponse, Http404
from django.contrib.auth.models import User, Group
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt # for testing only

from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import status

import json
import logging

from .models import Patient, Appointment, Physician

from health.serializers import UserSerializer, GroupSerializer, PatientSerializer, AppointmentSerializer, PhysicianSerializer

def index(request):
    return HttpResponse("Hello, world. You're at the health index.")

def patient_list(request):
    if request.method == 'GET':
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        context = {
            'patient_list': serializer.data,
        }
        return render(request, 'health/patient_list.html', context)
    elif request.method == 'POST':

        data = JSONParser().parse(request)
        serializer = PatientSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def visit_list(request):
    if request.method == 'GET':
        try:
            appointments = Appointment.appointment_by_doctor_by_day(request.session['physician_id'], request.session['selected_date'])
        except KeyError:
            appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)
        context = {
            'visit_list': serializer.data,
        }
        return render(request, 'health/visit_list.html', context)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AppointmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class AppointmentDetail(APIView):
    def get_object(self, pk):
        try:
            return Appointment.objects.get(pk=pk)
        except Appointment.DoesNotExist:
            return Http400

    def get(self, request, pk, format=None):
        apt = self.get_object(pk)
        serializer = AppointmentSerializer(apt)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        apt = self.get_object(pk)
        serializer = Appointment(apt, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        apt = self.get_object(pk)
        apt.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class based patient view
class PatientDetail(APIView):
    def get_object(self, pk):
        try:
            return Patient.objects.get(pk=pk)
        except Patient.DoesNotExist:
            return Http400

    def get(self, request, pk, format=None):
        patient = self.get_object(pk)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        patient = self.get_object(pk)
        serializer = PatientSerializer(patient, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        patient = self.get_object(pk)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PhysicianViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Physician.objects.all().order_by('last_name')
    serializer_class = PhysicianSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer