from django.db import models
from django.contrib.auth.models import User
from Home.models import City,State
# Create your models here.
class Customer_Profile(models.Model):
    gender_op=(('M','Male'),('F','Female'),('O','Other'),)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    usname=models.CharField(max_length=30,default="USER",null=True)
    gender=models.CharField(max_length=1,choices=gender_op,null=True)
    image=models.ImageField(upload_to='Customers/',null=True,default='user-default.jpg')
    contact=models.CharField(max_length=10,null=True)
    address=models.TextField(null=True)
    city=models.ForeignKey(City,on_delete=models.CASCADE,null=True,default=0)
    state=models.ForeignKey(State,on_delete=models.CASCADE,null=True,default=0)

class Tokens(models.Model):
    username=models.CharField(max_length=50)
    token=models.CharField(max_length=250)
    