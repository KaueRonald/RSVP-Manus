from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models              import Event
from .forms               import EventForm


@login_required
def event_list(request):
    qs = Event.objects.all().order_by("date")
    return render(request, "events/list.html", {"events": qs})

@login_required
def event_create(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("events:list")
    else:
        form = EventForm()
    return render(request, "events/create.html", {"form": form})