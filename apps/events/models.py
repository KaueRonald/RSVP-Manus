from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

# Removed import: from apps.guests.models import Category, GuestGroup
# Category and GuestGroup are now defined within this app.

class Event(models.Model):
    
    EVENT_TYPES = [
        ("CONF", "Conferência"),
        ("MEET", "Encontro"),
        ("webinar", "Webinar"),
    ]

    name        = models.CharField("Nome do Evento", max_length=200)
    description = models.TextField("Descrição", blank=True)
    location    = models.CharField("Local", max_length=200)
    date        = models.DateTimeField("Data e Hora")
    capacity    = models.PositiveIntegerField("Capacidade")
    type        = models.CharField("Tipo", max_length=50, choices=EVENT_TYPES)

    def clean(self):
        # validações customizadas:
        if self.date <= timezone.now():
            raise ValidationError({"date": "A data deve ser no futuro."})
        if self.capacity <= 0:
            raise ValidationError({"capacity": "A capacidade deve ser maior que zero."})

    def __str__(self):
        return f"{self.name} @ {self.date:%Y-%m-%d %H:%M}"

class Category(models.Model):
    event = models.ForeignKey(
        "events.Event", on_delete=models.CASCADE,
        related_name="categories",
        verbose_name="Evento"
    )
    name  = models.CharField(max_length=100)
    # Making name unique per event, not globally
    # Consider adding unique_together = ('event', 'name') in Meta if needed

    class Meta:
        # Ensure category names are unique within the scope of a single event
        unique_together = ('event', 'name')
        verbose_name = "Categoria (Evento)"
        verbose_name_plural = "Categorias (Evento)"

    def __str__(self):
        return f"{self.name} (Evento: {self.event.name[:20]}...)"

class GuestGroup(models.Model):
    event    = models.ForeignKey(
        "events.Event", on_delete=models.CASCADE,
        related_name="guest_groups",
        verbose_name="Evento"
    )
    # Category must belong to the same event
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        related_name="groups",
        limit_choices_to={'event_id': models.F('event_id')} # Ensure category is from the same event
    )
    name     = models.CharField(max_length=100)
    # Making name unique per event, not globally
    # Consider adding unique_together = ('event', 'name') in Meta if needed

    class Meta:
        # Ensure group names are unique within the scope of a single event
        unique_together = ('event', 'name')
        verbose_name = "Grupo de Convidados (Evento)"
        verbose_name_plural = "Grupos de Convidados (Evento)"

    def clean(self):
        # Ensure the selected category belongs to the same event as the group
        if self.category_id and self.event_id:
            if self.category.event != self.event:
                raise ValidationError({
                    'category': 'A categoria selecionada não pertence a este evento.'
                })

    def __str__(self):
         return f"{self.name} (Categoria: {self.category.name}, Evento: {self.event.name[:20]}...)"

