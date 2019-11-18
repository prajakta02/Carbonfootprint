from django.db import models

# Create your models here.
class Emission(models.Model):
    electricity_emission=models.FloatField()
    plastic_emission=models.FloatField()
    two_wheeler_emission=models.FloatField()
    four_wheeler_emission=models.FloatField()
    train_emission=models.FloatField()
    bus_emission=models.FloatField()
    trees_absorption=models.FloatField()
    