from django.db import models
from track.models import TimeStampMixin

# Create your models here.
class CollectRequest(TimeStampMixin,models.Model):
    clientt     = models.ManyToManyField()
    collector   = models.IntegerField(default=0,null=True, blank=True)
    date

    def __str__(self):
        return self.name