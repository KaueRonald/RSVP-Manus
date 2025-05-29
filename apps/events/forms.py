from django import forms
from .models import Event, Category, GuestGroup

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]

class GuestGroupForm(forms.ModelForm):
    class Meta:
        model = GuestGroup
        fields = ["name", "category"]

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["name", "description", "location", "date", "capacity", "type"]
        widgets = {
            # coloca um input “datetime-local” pro campo date
            "date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }