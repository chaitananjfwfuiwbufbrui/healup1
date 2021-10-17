from django.db import models

# from main.models import Slot_booking
from main.models import *
# Create your models here.
class report(models.Model):
    name = models.CharField(max_length=20)
    patient = models.ForeignKey(Slot_booking,on_delete=models.SET_NULL,blank=True,null=True)
    service = models.ForeignKey(Services,on_delete=models.SET_NULL,blank=True,null=True)
    description = models.TextField()
    image = models.ImageField(upload_to="shop/images",default="")