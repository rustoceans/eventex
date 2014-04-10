# coding: utf-8
from django.views.generic import CreateView, DetailView
from .models import Subscription
from .forms import SubscriptionForm


class SubscriptionCreate(CreateView):
    model = Subscription
    form_class = SubscriptionForm


class SubscriptionDetail(DetailView):
    model = Subscription
