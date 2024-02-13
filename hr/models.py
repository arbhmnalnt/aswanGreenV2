from django.db import models
from track.models import TimeStampMixin

class Departement(TimeStampMixin,models.Model):
    name  = models.CharField(max_length=50)
    notes = models.TextField(max_length=50,null=True, blank=True)
    
    def __str__(self):
        return str(self.name)

class Employee(TimeStampMixin,models.Model):
    WORKER = "عامل"
    EMPLOYEE = "موظف"
    CHOICES_EMP = (
        (WORKER, "عامل"),
        (EMPLOYEE, "موظف")
    )
    name    = models.CharField(max_length=50 , null=True, blank=True,  verbose_name="الاسم")
    typee   = models.CharField(max_length=50 , null=True, blank=True, choices=CHOICES_EMP)
    dep  = models.ForeignKey('Departement', on_delete=models.CASCADE,  null=True, blank=True)
    jobTitle     = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.name)

