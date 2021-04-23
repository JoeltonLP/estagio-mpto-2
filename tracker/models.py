from django.db import models


class State(models.Model):
    name = models.CharField('name', max_length=100, unique=True)
    abbreviation = models.CharField('abbreviation', max_length=2, unique=True)
