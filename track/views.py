from django.shortcuts import render
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView
from django.db.models import Q



class TrackListView(LoginRequiredMixin, ListView):
    model = Track
    template_name = 'track/track_list.html'
    context_object_name = 'records'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(person__icontains=search_query) | Q(depart__icontains=search_query)
            )
        return queryset


def addTrack(depart, person, details):
        record = Track.objects.create(
            depart = depart,
            person = person,
            details = details
        )
        recordId = record.id
        return recordId
