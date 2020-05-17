from django.db import models
from django.contrib.auth.models import User


Status_Choice=(

    ('Y','Payed'),
    ('N','NotPayed'),
    ('E',"ERROR")
)

class Payment_Details(models.Model):

    user=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    date=models.DateTimeField()
    amount=models.BigIntegerField()
    Token = models.CharField(max_length=80)
    OrderID = models.BigIntegerField()
    Status = models.CharField(max_length=1,choices=Status_Choice)

    def __str__(self):
        return '{} , {} , {}'.format(self.user,self.amount,self.Token)