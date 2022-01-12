from django.db import models
from django.db import models
from Customer.models import Customer_Profile
from ServiceProvider.models import OperatorProfile,Attendant,OperatorService
from Home.models import Offer
from datetime import date
# Create your models here.
class Appointment(models.Model):
    ap_id=models.AutoField(primary_key=True)
    op_sr=models.ForeignKey(OperatorService,on_delete=models.CASCADE)
    user=models.ForeignKey(Customer_Profile,on_delete=models.CASCADE)
    bdate=models.DateField()
    adate=models.DateField(blank=True,default=date.today())
    offer=models.ForeignKey(Offer,on_delete=models.CASCADE,blank=True,null=True)
    status=models.IntegerField(default=1)
class Feedback(models.Model):
    feed_id=models.AutoField(primary_key=True)
    ap_id=models.ForeignKey(Appointment,on_delete=models.CASCADE)
    rate=models.CharField(max_length=1)
class ReserveLog(models.Model):
    os_id=models.IntegerField()
    rdate=models.DateField()