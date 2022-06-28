from distutils.command.upload import upload
from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.

class Venta(models.Model):
    tipo_prop_v= models.CharField(max_length=40)
    localidad_v= models.CharField(max_length=40)
    barrio_v= models.CharField(max_length=40)
    cant_dormi_v= models.IntegerField()
    estado_v= models.BooleanField()
    otro_cha_v= models.CharField(max_length=40)
    otro_ent_v= models.IntegerField()
    descrp_v= models.TextField(max_length=400, default="anything")

class Alquiler(models.Model):
    tipo_prop_a= models.CharField(max_length=40)
    localidad_a= models.CharField(max_length=40)
    barrio_a= models.CharField(max_length=40)
    cant_dormi_a= models.IntegerField()
    estado_a= models.BooleanField()
    otro_cha_a= models.CharField(max_length=40)
    otro_ent_a= models.IntegerField()
    descrp_a= models.TextField(max_length=400, default="anything")

class Turismo(models.Model):
    tipo_prop_t= models.CharField(max_length=40)
    localidad_t= models.CharField(max_length=40)
    barrio_t= models.CharField(max_length=40)
    cant_dormi_t= models.IntegerField()
    estado_t= models.BooleanField()
    otro_cha_t= models.CharField(max_length=40)
    otro_ent_t= models.IntegerField()
    descrp_t= models.TextField(max_length=400, default="anything")


#Creadion del Avatar
class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen= models.ImageField(upload_to= 'avatares', null=True, blank=True)
