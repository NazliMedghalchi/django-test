# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime


# Create your models here.

class DailyCheckin(models.Model):
    user_id = models.TextField()
    user_name = models.CharField(max_length=25)
    start = models.DateTimeField(default=datetime.now, blank=True)
    end = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.user_name


class Happiness(models.Model):
    submit_id = models.IntegerField(primary_key=True)
    user_id = models.TextField(max_length=10)
    level = models.IntegerField(default=5)

    def __str__(self):
        return self.user_id
