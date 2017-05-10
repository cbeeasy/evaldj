from django.db import models

# Create your models here.
class MyDatas(models.Model):
    vib1 = models.FloatField("Vibrations", default=0.0)
    vib2 = models.FloatField("Vibrations2", default=0.0)