from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('list/', views.event_list, name='list'),
    path("create/", views.event_create, name="create"),
    path("categories/", views.category_list, name="category_list"),
    path("categories/create/", views.category_create, name="category_create"),
    path("categories/<int:pk>/edit/",   views.category_update, name="category_update"),
    path("categories/<int:pk>/delete/", views.category_delete, name="category_delete"),
    path("groups/", views.group_list, name="group_list"),
    path("groups/create/", views.group_create, name="group_create"),
    path("groups/<int:pk>/edit/",   views.group_update,   name="group_update"),
    path("groups/<int:pk>/delete/", views.group_delete,   name="group_delete"),
]
