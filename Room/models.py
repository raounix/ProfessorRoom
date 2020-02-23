from django.db import models
from django.contrib.auth.models import User

import datetime
# Create your models here.


class Users(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    cell_phone = models.CharField(max_length=10)
    SSN = models.CharField(max_length=10)
    Address = models.TextField()
    profile = models.ImageField(upload_to="imgs/",blank=True,null=True)
    room_alotted = models.BooleanField(default=False)
    Room = models.OneToOneField('Room',blank=True,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return str(self.user)


class Room(models.Model):
    room_choice = [('1','یک تخته'),('2',"دو تخته"),("3","سه تخته"),("4","چهار تخته")]
    no = models.CharField(max_length=5)
    name = models.CharField(max_length=255)
    room_type = models.CharField(choices=room_choice,max_length=1,default=None)
    vacant = models.BooleanField(default=False)
    reserved_for_specific_user = models.OneToOneField(Users,default=None,on_delete=models.CASCADE,null=True,blank=True)
    images = models.ImageField(upload_to="hotel_image/",default=None)
    default_price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Reserve(models.Model):
    reserve_id = models.AutoField(primary_key=True)
    room = models.OneToOneField(Room,on_delete=models.DO_NOTHING)
    user = models.OneToOneField(Users,on_delete=models.DO_NOTHING)
    start_time = models.DateField(blank=True)
    end_time = models.DateField(blank=True)
    total_price = models.IntegerField()
    bednumber = models.IntegerField(default=2)
    people_count = models.IntegerField(default=0)
    payed = models.BooleanField(default=0)
    def __str__(self):
        return self.room.name

class payment(models.Model):
    order_id = models.AutoField(primary_key=True)
    reserve = models.OneToOneField(Reserve,on_delete=models.DO_NOTHING)
    payed_price = models.IntegerField()
    """discountcode = models.OneToOneField(Discount,on_delete=models.DO_NOTHING)"""

class Discount(models.Model):
    discount_code = models.CharField(primary_key=True,max_length=50)
    discount_type = models.IntegerField(choices=[('1','درصدی'),('2','مبلغی')])
    discount_value = models.IntegerField()
