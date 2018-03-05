from __future__ import unicode_literals
from urllib.parse import quote_plus
from django import template
from django.contrib.auth.models import Group,User
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.views.generic import CreateView, FormView, ListView, DetailView,UpdateView
from home.forms import *
from home.models import *

register = template.Library()
