from django.db import models

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=250)
    organization_type =models.CharField(max_length=250)
    established = models.CharField(max_length=250)
    organization_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.name + '  -  ' +self.established

class Special_event(models.Model):
    organization = models.ForeignKey(Organization,on_delete=models.CASCADE)
    date = models.CharField(max_length=500)
    time =models.CharField(max_length=200)
    topic = models.CharField(max_length=20000)
    location = models.CharField(max_length=500)

    def __str__(self):
        return self.date