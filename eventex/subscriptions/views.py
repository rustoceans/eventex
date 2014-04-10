# coding: utf-8
from django.views.generic import CreateView, DetailView
from .forms import SubscriptionForm
from .models import Subscription


class SubscriptionCreate(CreateView):
    model = Subscription
    form_class = SubscriptionForm


class SubscriptionDetail(DetailView):
    model = Subscription
