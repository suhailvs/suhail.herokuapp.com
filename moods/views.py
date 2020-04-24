from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Mood

class MoodView(CreateView):
    model = Mood
    fields = ['moodswing', ]
    success_url = reverse_lazy('moods')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['moods'] = Mood.objects.order_by('-created_at')
        return context

