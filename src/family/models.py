from django.db import models


class family_member(models.Model):
    name = models.CharField(max_length=100)
    dni = models.IntegerField()
    birth_date = models.DateField()
