from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Entry
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin


@csrf_exempt
def public_api(request):
    if request.method == 'POST':
        return HttpResponse('API hit with post method')


class HomeView(LoginRequiredMixin, ListView):
    model = Entry
    template_name = 'entries/index.html'
    context_object_name = "blog_entries"
    ordering = ['-entry_date']
    paginate_by = 2


class EntryView(LoginRequiredMixin, DetailView):
    model = Entry
    template_name = 'entries/entry_detail.html'


class CreateEntryView(LoginRequiredMixin, CreateView):
    model = Entry
    template_name = 'entries/create_entry.html'
    fields = ['entry_title', 'entry_text']

    def form_valid(self, form):
        form.instance.entry_author = self.request.user
        return super().form_valid(form)

