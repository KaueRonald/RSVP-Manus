from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('apps.users.urls', namespace='users')),
    path('events/', include('apps.events.urls', namespace='events')),
    path('', RedirectView.as_view(pattern_name='users:login', permanent=False)),
]