from django.db import models
from track.models import TimeStampMixin

class Area(TimeStampMixin,models.Model):
    name = models.CharField(max_length=100,null=True, blank=True)
    counter = models.IntegerField(default=0,null=True, blank=True)

    def __str__(self):
        return self.name

class Service(models.Model):
    name                     = models.CharField(max_length=50,null=True, blank=True)
    typee                    = models.CharField(max_length=50,null=True, blank=True, default="شهرى")
    priceType                = models.CharField(max_length=50,null=True, blank=True, default="شهرى")
    price                    = models.IntegerField(null=True, blank=True)
    notes                    = models.TextField(max_length=250,null=True, blank=True)
    def __str__(self):
        return self.name + " : " + str(self.price)
    
    
class Client(TimeStampMixin,models.Model):
    serial      = models.IntegerField(null=True, blank=True, unique=True, db_index=True, verbose_name="الرقم التعريفى")
    name        = models.CharField(max_length=100,null=True, blank=True, db_index=True)
    phone       = models.CharField(max_length=100, null=True, blank=True, db_index=True)
    place       = models.ForeignKey('Area', related_name='area', on_delete=models.CASCADE,null=True, blank=True)
    street      = models.CharField(max_length=150, null=True, blank=True)
    building    = models.CharField(max_length=150,null=True, blank=True, help_text="تفاصيل العمارة السكنية")
    apart       = models.CharField(max_length=150,null=True, blank=True, help_text="تفاصيل الشقه")   # apartment
    details     = models.TextField(max_length=250,null=True, blank=True, help_text="اى تفاصيل إخرى للعنوان")
    notes       = models.TextField(max_length=250,null=True, blank=True)
    serviceId   = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class Contract(TimeStampMixin,models.Model):
    clientt          = models.ForeignKey('Client', related_name='client', on_delete=models.CASCADE,null=True, blank=True,db_index=True)
    servicee         = models.ForeignKey('Service', related_name='service', on_delete=models.CASCADE,null=True, blank=True)
    notes           = models.TextField(max_length=250,null=True, blank=True)

    def __str__(self):
        return str(self.pk)

class FollowContractServices(TimeStampMixin,models.Model):
    COLLECT_STATUS = (
        ('wecd', 'فى انتظار ميعاد التحصيل'),  # waiting Estimated collection date
        ('pr', 'مطلوب الدفع'),                 # Payment required
        ('pip', 'جارى الدفع'),                 # Payment in progress
        ('pd', 'تم الدفع'),                    # payment done
        ('lp', 'متأخر الدفع')                  # late payment
    )

    clientt               = models.ForeignKey('Client', related_name='fclient', on_delete=models.CASCADE,null=True, blank=True, db_index=True)
    contractt               = models.ForeignKey('Contract', related_name='fcontract', on_delete=models.CASCADE,null=True, blank=True, db_index=True)
    ecd                  = models.DateField(null=True, blank=True, verbose_name="تاريخ  التحصيل المفترض")        # Estimated collection date
    collcetStatus        = models.CharField(max_length=5,null=True, blank=True, db_index=True, choices=COLLECT_STATUS, default = 'wecd')
    deservedAmount       = models.IntegerField(null=True, blank=True, verbose_name="المبلغ المطلوب تحصيله")
    notes                = models.CharField(max_length=100,null=True, blank=True)





