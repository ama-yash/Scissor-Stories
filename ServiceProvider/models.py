from django.db import models
from django.contrib.auth.models import User
from Home.models import City,State,Service
# Create your models here.
class OperatorProfile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    uname=models.CharField(max_length=30,default="USER")
    image=models.ImageField(upload_to='Service Providers/',blank=True,default='user-default.jpg')
    firm_name=models.CharField(max_length=50)
    owner_name=models.CharField(max_length=50)
    contact=models.CharField(max_length=10)
    address=models.TextField()
    joined_on=models.DateTimeField(null=True,blank=True)
    city=models.ForeignKey(City,on_delete=models.CASCADE)
    state=models.ForeignKey(State,on_delete=models.CASCADE)
    is_active=models.BooleanField(default=True)
    bio=models.TextField(blank=True)
    def __str__(self):
        return self.firm_name
class Attendant(models.Model):
    at_id=models.AutoField(primary_key=True)
    ser_pro=models.ForeignKey(OperatorProfile,on_delete=models.CASCADE)
    at_name=models.CharField(max_length=50)
    contact=models.CharField(max_length=10)
    gender=models.CharField(max_length=1)
    image=models.ImageField(upload_to='Attendants/',default='user-default.jpg')
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return str(self.at_id)
class OperatorService(models.Model):
    op_ser=models.AutoField(primary_key=True)
    provider=models.ForeignKey(OperatorProfile,on_delete=models.CASCADE)
    ser_id=models.ForeignKey(Service,on_delete=models.CASCADE)
    attendant=models.ForeignKey(Attendant,on_delete=models.CASCADE)
    time_from=models.TimeField()
    time_to=models.TimeField()
    price=models.DecimalField(decimal_places=2,default=0.00,max_digits=8)
    is_active=models.BooleanField(default=True)

