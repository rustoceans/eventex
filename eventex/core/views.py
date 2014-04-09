# coding: utf-8
from django.shortcuts import render, get_object_or_404
from datetime import time
from .models import Speaker, Talk


def home(request):
    return render(request, 'index.html')


def speaker_detail(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    context = {'speaker': speaker}
    return render(request, 'core/speaker_detail.html', context)


def talk_list(request):
    midday = time(12)
    context = {
        'morning_talks': Talk.objects.filter(start_time__lt=midday),
        'afternoon_talks': Talk.objects.filter(start_time__gte=midday)
    }
    return render(request, 'core/talk_list.html', context)
