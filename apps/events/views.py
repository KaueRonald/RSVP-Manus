from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Event, Category, GuestGroup
from .forms  import EventForm
from .forms import CategoryForm, GuestGroupForm


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
def category_list(request):
    qs = Category.objects.all()
    return render(request, "events/category_list.html", {"categories": qs})

@login_required
def category_create(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("events:category_list")
    return render(request, "events/category_form.html", {"form": form})

@login_required
def group_list(request):
    qs = GuestGroup.objects.select_related("category").all()
    return render(request, "events/group_list.html", {"groups": qs})

@login_required
def group_create(request):
    form = GuestGroupForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("events:group_list")
    return render(request, "events/group_form.html", {"form": form})

@login_required
def category_update(request, pk):
    cat = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.POST or None, instance=cat)
    if form.is_valid():
        form.save()
        return redirect("events:category_list")
    return render(request, "events/category_form.html", {"form": form})

@login_required
def category_delete(request, pk):
    cat = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        cat.delete()
        return redirect("events:category_list")
    return render(request, "events/category_confirm_delete.html", {"object": cat})

@login_required
def group_update(request, pk):
    grp = get_object_or_404(GuestGroup, pk=pk)
    form = GuestGroupForm(request.POST or None, instance=grp)
    if form.is_valid():
        form.save()
        return redirect("events:group_list")
    return render(request, "events/group_form.html", {"form": form})

@login_required
def group_delete(request, pk):
    grp = get_object_or_404(GuestGroup, pk=pk)
    if request.method == "POST":
        grp.delete()
        return redirect("events:group_list")
    return render(request, "events/group_confirm_delete.html", {"object": grp})