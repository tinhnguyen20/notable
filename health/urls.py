from django.urls import path

from . import views

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
	path('appointments/', views.visit_list),
	path('appointments/<int:pk>', views.AppointmentDetail.as_view()),
    path('patients/', views.patient_list),
    path('patients/<int:pk>', views.PatientDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
