from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Thing


class ThingListView(ListView):
    template_name = "thing_list.html"
    model = Thing
    context_object_name = "things"


class ThingDetailView(DetailView):
    template_name = "thing_detail.html"
    model = Thing


class ThingCreateView(CreateView):
    template_name = "thing_create.html"
    model = Thing

    # NEW! this represents the fields that will be rendered in the form
    fields = ["name", "rating", "reviewer"]


class ThingDeleteView(DeleteView):
    template_name = "thing_delete.html"
    model = Thing
    success_url = reverse_lazy("thing_list")  # look up why!


class ThingUpdateView(UpdateView):
    # Looks exactly like CreateView
    template_name = "thing_update.html"
    model = Thing
    fields = "__all__"  # this would also work in the ThingCreateView
