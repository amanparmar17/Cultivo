from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import signin as sign
from .models import login as log
from .models import contacts as con
from django.urls import reverse
from django.views import generic
from django.utils import timezone
import datetime
from django.contrib.auth.models import User

class TemplateView(generic.TemplateView):
    name='cultivo/index.html'

