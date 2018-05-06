# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import DailyCheckin
from .models import Happiness

# Register your models here.

admin.site.register(DailyCheckin)
admin.site.register(Happiness)