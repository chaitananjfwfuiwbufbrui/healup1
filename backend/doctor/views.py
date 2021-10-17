from django.shortcuts import render
import doctor
from main.models import  *
# from .seralizer import *
from django.shortcuts import  render
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
import io
from django.views.decorators.csrf import csrf_exempt
import json
# from .seralizer import *
from rest_framework import permissions
from rest_framework.decorators import  api_view,permission_classes
from authentications.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
from datetime import datetime ,timedelta,date
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser,FileUploadParser
from rest_framework.response import Response
# from .mlmodels import *
from .seralizer import *
# <--------------------------------service list started --------------------->
class Patence(APIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = (MultiPartParser, FormParser)
    def get(self,request,patientname = None):
        # if patientname:
        #     print("hlo")
        #     slot = Slot_booking.object.filter(patient = patientname).first()
        s = Services.objects.filter(Doctor = request.user).first()
        customes = customer_seralizer(s)
        return JsonResponse(customes.data,safe=False)
# <--------------------------------service list end --------------------->
# <--------------------------------reposts list started --------------------->
class Reports(APIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = (MultiPartParser, FormParser)
    def get(self,request,patientname = None):
        patient_p = UserAccount.objects.filter(first_name = patientname).first()
        s = Services.objects.filter(Doctor = request.user).first()
        slot = Slot_booking.objects.filter(service_p =s,patient = patient_p).first()
        print(patient_p,slot)
        customes = reposts_seralizer(slot)
        return JsonResponse(customes.data,safe=False)
    def post(self,request,patientname = None):
        patient_p = UserAccount.objects.filter(first_name = patientname).first()
        s = Services.objects.filter(Doctor = request.user).first()
        slot = Slot_booking.objects.filter(service_p =s,patient = patient_p).first()
        python_data =request.data
        doc = request.FILES
        reports = report.objects.create(name =  python_data['name'],
        patient = slot,
        service = s,
        description = python_data['description'],
        image = doc['image']) 
        sa = Reposts_seralizer(reports)
        return JsonResponse(sa.data,safe=False)


# <--------------------------------reposts list end --------------------->