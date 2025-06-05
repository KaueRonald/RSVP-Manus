from django import forms
from .models import Event, Category, GuestGroup

class CategoryForm(forms.ModelForm):
    # No changes needed here for now, it just needs a name.
    # The association with the event happens in the view.
    class Meta:
        model = Category
        fields = ["name"]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da Categoria'}),
        }

class GuestGroupForm(forms.ModelForm):
    # We need to filter the 'category' field based on the event.
    # We'll pass the event instance to the form's __init__ method.
    def __init__(self, *args, **kwargs):
        event = kwargs.pop('event', None) # Get the event passed from the view
        super().__init__(*args, **kwargs)
        if event:
            # Filter the category queryset to show only categories belonging to the specific event
            self.fields['category'].queryset = Category.objects.filter(event=event)
        else:
            # If no event is passed (e.g., maybe a global admin view?), show all or none?
            # For now, let's default to an empty queryset if no event is provided in this context.
            # Or perhaps raise an error, as a group should always belong to an event now.
            self.fields['category'].queryset = Category.objects.none()
            # Alternatively, could fetch based on instance if editing:
            # if self.instance and self.instance.pk and self.instance.event:
            #     self.fields['category'].queryset = Category.objects.filter(event=self.instance.event)

    class Meta:
        model = GuestGroup
        fields = ["name", "category"]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Grupo'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }

class EventForm(forms.ModelForm):
    name = forms.CharField(
        label="Nome do Evento",
        widget=forms.TextInput(attrs={
            "class": "form-control floating-label-input", # Added form-control for consistency
            "placeholder": " ",
        }),
    )
    description = forms.CharField(
        label="Descrição",
        required=False,
        widget=forms.Textarea(attrs={
            "class": "form-control floating-label-input",
            "placeholder": " ",
            "rows": 3,
        }),
    )
    location = forms.CharField(
        label="Local",
        widget=forms.TextInput(attrs={
            "class": "form-control floating-label-input",
            "placeholder": " ",
        }),
    )
    date = forms.DateTimeField(
        label="Data e Hora",
        widget=forms.DateTimeInput(attrs={
            "type": "datetime-local",
            "class": "form-control floating-label-input",
            "placeholder": " ",
        }),
    )
    capacity = forms.IntegerField(
        label="Capacidade",
        widget=forms.NumberInput(attrs={
            "class": "form-control floating-label-input",
            "placeholder": " ",
        }),
    )
    type = forms.ChoiceField(
        label="Tipo",
        choices=Event.EVENT_TYPES,
        widget=forms.Select(attrs={"class": "form-select floating-label-input"}), # Changed to form-select
    )

    class Meta:
        model = Event
        fields = ["name", "description", "location", "date", "capacity", "type"]
        # The widgets dict here might override the individual field definitions above,
        # ensure consistency or remove redundancy.
        widgets = {
            "date": forms.DateTimeInput(attrs={"type": "datetime-local", "class": "form-control"}),
        }

    # Note: The Formsets defined here are not currently used in the provided views.
    # They might be intended for inline editing on the event creation/update page.
    # If needed, they would require corresponding handling in the views and templates.
    # CategoryFormset = forms.inlineformset_factory(
    #     Event, Category, form=CategoryForm, fields=["name"], extra=1, can_delete=True
    # )
    # GuestGroupFormset = forms.inlineformset_factory(
    #     Event, GuestGroup, form=GuestGroupForm, fields=["name","category"], extra=1, can_delete=True
    # )

