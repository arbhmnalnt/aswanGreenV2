from django.db import models
from track.models import TimeStampMixin
from clientManager.models import *
from hr.models import Employee

# Create your models here.
class CollectRequest(TimeStampMixin,models.Model):
    name            = models.CharField(max_length=100,null=True, blank=True, verbose_name="تحصيل شهر ")
    clientt         = models.ManyToManyField(FollowContractServices, verbose_name="متابعات التحصيل") 
    collector       = models.ForeignKey(Employee,  on_delete=models.CASCADE ,verbose_name="المحصل")
    daftrSerial     = models.CharField(max_length=14,null=True, blank=True, verbose_name="سريال دفتر التحصيل")
    startDate       = models.DateTimeField(null=True, blank=True, verbose_name="تاريخ بدء التحصيل")

    def __str__(self):
        return self.name 