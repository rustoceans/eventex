# coding: utf-8
from django.views.generic import TemplateView, DetailView
from django.shortcuts import render
from .models import Speaker, Talk


class HomeView(TemplateView):
    template_name = 'index.html'


class SpeakerDetail(DetailView):
    model = Speaker


def talk_list(request):
    context = {
        'morning_talks': Talk.objects.at_morning(),
        'afternoon_talks': Talk.objects.at_afternoon()
    }
    return render(request, 'core/talk_list.html', context)


class TalkDetail(DetailView):
    model = Talk
