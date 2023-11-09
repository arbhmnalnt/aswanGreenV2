from django.db import models

class TimeStampMixin(models.Model):
    is_deleted      = models.BooleanField (default=False, db_index=True)
    created_at      = models.DateTimeField(auto_now_add=True,null=True)
    updated_at      = models.DateTimeField(auto_now=True,null=True)

class Track(TimeStampMixin, models.Model):
    depart =  models.CharField(max_length=50, null=True, blank=True, default="ادخال البيانات") # القسم
    person  = models.CharField(max_length=50, null=True, blank=True)
    details = models.TextField(max_length=350,null=True, blank=True)