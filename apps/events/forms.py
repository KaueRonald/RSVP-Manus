from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    name = forms.CharField(
        label="Nome do Evento",
        widget=forms.TextInput(attrs={
            "class": "floating-label-input",
            "placeholder": " ",
        }),
    )
    description = forms.CharField(
        label="Descrição",
        required=False,
        widget=forms.Textarea(attrs={
            "class": "floating-label-input",
            "placeholder": " ",
            "rows": 3,
        }),
    )
    location = forms.CharField(
        label="Local",
        widget=forms.TextInput(attrs={
            "class": "floating-label-input",
            "placeholder": " ",
        }),
    )
    date = forms.DateTimeField(
        label="Data e Hora",
        widget=forms.DateTimeInput(attrs={
            "type": "datetime-local",
            "class": "floating-label-input",
            "placeholder": " ",
        }),
    )
    capacity = forms.IntegerField(
        label="Capacidade",
        widget=forms.NumberInput(attrs={
            "class": "floating-label-input",
            "placeholder": " ",
        }),
    )
    type = forms.ChoiceField(
        label="Tipo",
        choices=Event.EVENT_TYPES,
        widget=forms.Select(attrs={"class": "floating-label-input"}),
    )

    class Meta:
        model = Event
        fields = ["name", "description", "location", "date", "capacity", "type"]
        widgets = {
            "date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }

    CategoryFormset = forms.inlineformset_factory(
    Event, Category, fields=["name"], extra=1, can_delete=True
)
    GuestGroupFormset = forms.inlineformset_factory(
    Event, GuestGroup, fields=["name","category"], extra=1, can_delete=True
)