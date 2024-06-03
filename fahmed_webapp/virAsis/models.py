from django.db import models

class ElecDom(models.Model):
    name=models.CharField(max_length=100)
    status=models.BooleanField(default=False)
    temperature=models.FloatField(null=True,blank=True)
    humidity=models.FloatField(null=True,blank=True)

    def __str__(self):
        return self.name

