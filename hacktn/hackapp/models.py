from django.db import models

# Create your models here.


class User(models.Model):
    surname=models.CharField(max_length=50,blank=True,null=True)
    name=models.CharField(max_length=50,blank=True,null=True)
    father_name=models.CharField(max_length=50,blank=True,null=True)
    serial_id=models.IntegerField(blank=True,null=True)
    city=models.CharField(max_length=50,blank=True,null=True)
    street=models.TextField(max_length=50,blank=True,null=True)
    home_n=models.CharField(max_length=10,blank=True,null=True)
    flat_n=models.CharField(max_length=10,blank=True,null=True)
    cad_n=models.CharField(max_length=20,blank=True,null=True)
    area_n=models.IntegerField(blank=True,null=True)
    lat=models.FloatField(blank=True,null=True)
    lng=models.FloatField(blank=True,null=True)
    addi_info=models.TextField(max_length=100,blank=False,null=True)
    def __str__(self):
        return 'User: ' + self.name


