from django.db.models import fields, manager
# from main.models import Orderitems, Products
from rest_framework import serializers
from .models import *

from main.seralizer import *
class customer_seralizer(serializers.ModelSerializer):
    patient = serializers.SerializerMethodField('get_likes')
    def get_likes(self, product):
        qs = Slot_booking.objects.filter(service_p=product)
        serializer = Slot_booking_seralizers(instance=qs, many=True)
        return serializer.data
    class Meta:
        model = Services()
        fields = ['Name_of_service','patient']


class Reposts_seralizer(serializers.ModelSerializer):
    patient_name = serializers.CharField(read_only=True, source='patient.get_full_name')
    class Meta:
        model = report()
        fields =  ['name' ,'patient' ,'service','description','image','patient_name']



class reposts_seralizer(serializers.ModelSerializer):
    reports = serializers.SerializerMethodField('get_reports')
    def get_reports(self,patient):
        reports = report.objects.filter(patient = patient)
        serializer = Reposts_seralizer(instance=reports, many=True)
        return serializer.data
    class Meta:
        model = Slot_booking()
       
        fields = ['date' ,'time_slot' ,'payed_amount','payment','reports']
        # fields = '__all__'
    
    

  
    
    