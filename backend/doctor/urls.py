from django.contrib import admin
from doctor import views
from django.urls import path,include
urlpatterns = [
    path('patents/', views.Patence.as_view(), name='patents'),
    path('reports/<str:patientname>/', views.Reports.as_view(), name='reports'),
]