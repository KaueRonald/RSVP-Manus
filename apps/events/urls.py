# Conteúdo original de apps/events/urls.py
from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('list/', views.event_list, name='list'),
    path("create/", views.event_create, name="create"),
    # Rota para detalhes do evento
    path("evento/<int:event_id>/", views.event_detail, name="detail"),

    # Rotas globais (manter ou remover/ajustar depois?)
    path("categories/", views.category_list, name="category_list"),
    path("categories/create/", views.category_create, name="category_create"),
    path("categories/<int:pk>/edit/",   views.category_update, name="category_update"),
    path("categories/<int:pk>/delete/", views.category_delete, name="category_delete"),
    path("groups/", views.group_list, name="group_list"),
    path("groups/create/", views.group_create, name="group_create"),
    path("groups/<int:pk>/edit/",   views.group_update,   name="group_update"),
    path("groups/<int:pk>/delete/", views.group_delete,   name="group_delete"),

    # Rotas para categorias e grupos específicos do evento
    path("evento/<int:event_id>/categories/create/", views.event_category_create, name="event_category_create"),
    path("evento/<int:event_id>/groups/create/", views.event_group_create, name="event_group_create"),
    # Adicionar rotas de update/delete para categorias/grupos do evento se necessário
]

