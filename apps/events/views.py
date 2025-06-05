from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import Event, Category, GuestGroup
from .forms import EventForm, CategoryForm, GuestGroupForm


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


@login_required
def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    categories = event.categories.all()  # Using related_name from Event model
    guest_groups = event.guest_groups.select_related('category').all() # Using related_name
    context = {
        "event": event,
        "categories": categories,
        "guest_groups": guest_groups,
    }
    return render(request, "events/event_detail.html", context)


@login_required
def event_category_create(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.event = event
            category.save()
            return redirect(reverse('events:detail', kwargs={'event_id': event_id}))
    else:
        form = CategoryForm()
    return render(request, "events/category_form.html", {"form": form, "event": event})


@login_required
def event_group_create(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == "POST":
        # Pass event to form for category filtering
        form = GuestGroupForm(request.POST, event=event)
        if form.is_valid():
            guest_group = form.save(commit=False)
            guest_group.event = event
            guest_group.save()
            return redirect(reverse('events:detail', kwargs={'event_id': event_id}))
    else:
        # Pass event to form for category filtering
        form = GuestGroupForm(event=event)
    return render(request, "events/group_form.html", {"form": form, "event": event})


# --- Potentially redundant global views --- 
# Consider removing or adjusting these later if they are no longer needed

@login_required
def category_list(request):
    # This might be confusing now. Maybe list categories grouped by event?
    qs = Category.objects.select_related('event').all()
    return render(request, "events/category_list.html", {"categories": qs})


@login_required
def category_create(request):
    # This creates a category without an event, which might be wrong now.
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        # Where to redirect? Maybe back to the global list?
        return redirect("events:category_list")
    # Need to adjust template if it assumes an event context
    return render(request, "events/category_form.html", {"form": form})


@login_required
def group_list(request):
    # Similar issue as category_list
    qs = GuestGroup.objects.select_related("category", "event").all()
    return render(request, "events/group_list.html", {"groups": qs})


@login_required
def group_create(request):
    # Similar issue as category_create. Also, category filtering won't work without an event.
    # This will likely fail or behave unexpectedly now due to form changes.
    form = GuestGroupForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("events:group_list")
    return render(request, "events/group_form.html", {"form": form})


@login_required
def category_update(request, pk):
    cat = get_object_or_404(Category, pk=pk)
    # Need to decide if editing should be global or per-event
    form = CategoryForm(request.POST or None, instance=cat)
    if form.is_valid():
        form.save()
        # Redirect to event detail if editing within event context?
        return redirect("events:category_list")
    return render(request, "events/category_form.html", {"form": form, "event": cat.event})


@login_required
def category_delete(request, pk):
    cat = get_object_or_404(Category, pk=pk)
    event_id = cat.event.id # Get event id before deleting
    if request.method == "POST":
        cat.delete()
        # Redirect to event detail?
        return redirect(reverse('events:detail', kwargs={'event_id': event_id}))
        # return redirect("events:category_list") # Old redirect
    # Need a confirmation template, maybe pass event context?
    return render(request, "events/category_confirm_delete.html", {"object": cat, "event": cat.event})


@login_required
def group_update(request, pk):
    grp = get_object_or_404(GuestGroup, pk=pk)
    event = grp.event # Get event for form filtering
    # Pass event to form for category filtering
    form = GuestGroupForm(request.POST or None, instance=grp, event=event)
    if form.is_valid():
        form.save()
        # Redirect to event detail?
        return redirect(reverse('events:detail', kwargs={'event_id': event.id}))
        # return redirect("events:group_list") # Old redirect
    return render(request, "events/group_form.html", {"form": form, "event": event})


@login_required
def group_delete(request, pk):
    grp = get_object_or_404(GuestGroup, pk=pk)
    event_id = grp.event.id # Get event id before deleting
    if request.method == "POST":
        grp.delete()
        # Redirect to event detail?
        return redirect(reverse('events:detail', kwargs={'event_id': event_id}))
        # return redirect("events:group_list") # Old redirect
    # Need a confirmation template, maybe pass event context?
    return render(request, "events/group_confirm_delete.html", {"object": grp, "event": grp.event})

