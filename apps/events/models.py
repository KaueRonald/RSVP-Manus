from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

from apps.guests.models import Category, GuestGroup

class Event(models.Model):

    categories = models.ManyToManyField(Category, blank=True)
    guest_groups = models.ManyToManyField(GuestGroup, blank=True)
    
    EVENT_TYPES = [
        ("CONF", "Conferência"),
        ("MEET", "Encontro"),
        ('webinar', 'Webinar'),
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
            raise ValidationError({'date': 'A data deve ser no futuro.'})
        if self.capacity <= 0:
            raise ValidationError({'capacity': 'A capacidade deve ser maior que zero.'})

    def __str__(self):
        return f"{self.name} @ {self.date:%Y-%m-%d %H:%M}"
