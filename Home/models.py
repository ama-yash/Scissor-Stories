from django.db import models

# Create your models here.
class State(models.Model):
    state_id=models.AutoField(primary_key=True)
    state_name=models.CharField(max_length=30)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.state_name
class City(models.Model):
    city_id=models.AutoField(primary_key=True)
    state=models.ForeignKey(State,on_delete=models.CASCADE)
    city_name=models.CharField(max_length=30)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.city_name
class Service(models.Model):
    ser_id=models.AutoField(primary_key=True)
    ser_name=models.CharField(max_length=20)
    poster=models.ImageField(blank=True,null=True,upload_to='Posters/',default='user-default.jpg')
    gender=models.CharField(max_length=1)
    is_active=models.BooleanField(default=True)
class Offer(models.Model):
    offer_id=models.CharField(primary_key=True,max_length=10)
    offer_name=models.CharField(max_length=50)
    offer_from=models.DateField()
    offer_to=models.DateField()
    disc_ratio=models.IntegerField()
    maxamount=models.IntegerField()
    is_active=models.BooleanField(default=True)
class Role(models.Model):
    role_id=models.IntegerField(primary_key=True)
    role_name=models.CharField(max_length=20)