from django.db import models
from track.models import TimeStampMixin
from clientManager.models import Client

# Create your models here.
class CollectRequest(TimeStampMixin,models.Model):
    clientt         = models.ManyToManyField(Client) 
    collector       = models.IntegerField(default=0,null=True, blank=True)
    daftr_serial    = models.CharField(max_length=14,null=True, blank=True)

    def __str__(self):
        return self.name 