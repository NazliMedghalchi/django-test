# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import DailyCheckin, Happiness


# Create your views here.

def index(request):
    user = DailyCheckin.objects.all()[:10]
    context = {
        'name': user
    }
    return HttpResponse(render, 'index.html', context)


def rates(request):
    rate = Happiness.objects.all()[:20]
    context = {
        'rate': rate
    }
    return HttpResponse(render, 'happiness.html', context)


def submit(request):
    if request == 'POST':
        user_id = request.POST['user_id']
        level = request.POST['level']
        happiness_rate = Happiness(user_id=user_id, level=level)

        happiness_rate.save()
        return render(request, 'happiness.html')
    else:
        return redirect('/happiness')


def show(request, submit_id):
    if request.method == 'GET':
        context = {
            'ratio': Happiness.objects.get(submit_id=submit_id)
        }
        return render(request, 'happiness.html', context)
    else:
        return redirect('/happiness')
