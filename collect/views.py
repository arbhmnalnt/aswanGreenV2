from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from clientManager.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView, CreateView
from clientManager.models import *
from django.db.models import Q
from clientManager.forms import *
from datetime import date, datetime
from track.views import addTrack
from django.contrib.auth.mixins import LoginRequiredMixin
import sys

