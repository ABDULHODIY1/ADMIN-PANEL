from django.shortcuts import render
from django.views.generic import *
# Create your views here.

class Collectuser(TemplateView):
    template_name = "TelegramUsers.html"
