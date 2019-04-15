from django.db import models

# Create your models here.
class Temperature(models.Model):
    deviceId = models.CharField(max_length=100)
    temperature = models.IntegerField()
    eventTime = models.DateTimeField()

    def __str__(self):
        return self.deviceId + str(self.eventTime)