from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

from apps.guests.models import Category, GuestGroup

class Event(models.Model):
    
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

class Category(models.Model):
    event = models.ForeignKey(
        'events.Event', on_delete=models.CASCADE,
        related_name='categories',
        verbose_name="Evento"
    )
    name  = models.CharField(max_length=100, unique=True)
    # …

class GuestGroup(models.Model):
    event    = models.ForeignKey(
        'events.Event', on_delete=models.CASCADE,
        related_name='guest_groups',
        verbose_name="Evento"
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='groups')
    name     = models.CharField(max_length=100, unique=True)
    # …