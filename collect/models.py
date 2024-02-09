from django.db import models
from track.models import TimeStampMixin
from clientManager.models import Client
from hr.models import Employee

# Create your models here.
class CollectRequest(TimeStampMixin,models.Model):
    clientt         = models.ManyToManyField(Client) 
    collector       = models.ForeignKey(Employee,  on_delete=models.CASCADE ,verbose_name="المحصل")
    daftr_serial    = models.CharField(max_length=14,null=True, blank=True, verbose_name="سريال دفتر التحصيل")

    def __str__(self):
        return self.name 