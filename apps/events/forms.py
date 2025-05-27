from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["name", "description", "location", "date", "capacity", "type"]
        widgets = {
            # coloca um input “datetime-local” pro campo date
            "date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }