from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Users(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    cell_phone = models.CharField(max_length=10)
    SSN = models.CharField(max_length=10)
    Address = models.TextField()
    profile = models.ImageField(upload_to="imgs/")
    room_alotted = models.BooleanField(default=False)
    Room = models.OneToOneField('Room',blank=True,on_delete=models.CASCADE,null=True)


class Room(models.Model):
    room_choice = [('1','یک تخته'),('2',"دو تخته"),("3","۳ تخته"),("4","۴ تخته")]
    no = models.CharField(max_length=5)
    name = models.CharField(max_length=255)
    room_type = models.CharField(choices=room_choice,max_length=1,default=None)
    vacant = models.BooleanField(default=False)
    reserved_for_specific_user = models.OneToOneField(Users,default=None,on_delete=models.CASCADE)
    hostel = models.ForeignKey('Hostel', on_delete=models.CASCADE)
    images = models.ImageField(upload_to="hotel_image/",default=None)

    def __str__(self):
        return self.name


class Hostel(models.Model):
    name = models.CharField(max_length=5)
    gender_choices = [('M', 'مذکر'), ('F', 'مونث'),("MF","هر دو جنسیت")]
    gender = models.CharField(
        choices=gender_choices,
        max_length=2,
        default=None,
        null=True)
    warden = models.CharField(max_length=100, blank=True)
    caretaker = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
