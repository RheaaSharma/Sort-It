from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import FormMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView

# from .forms import ComposeForm
# from .models import Thread, ChatMessage

from django.shortcuts import render
import os
import django
os.environ["DJANGO_SETTINGS_MODULE"] = 'arizona.settings'
django.setup()


def index(request):
    return render(request, 'canyon/index.html')


def results(request):
    return render(request, 'canyon/results.html')
