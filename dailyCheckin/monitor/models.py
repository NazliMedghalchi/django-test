# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
# Create your models here.

class DailyCheckin(models.Model):
    user_id = models.IntegerField()
    start = models.DateTimeField(default=datetime.now, blank=True)
    end = models.DateTimeField(default=datetime.now, blank=True)
    submit_id = models.IntegerField()

class Happiness(models.Model):
    user_id = models.IntegerField()
    level = models.IntegerField(default=5)
