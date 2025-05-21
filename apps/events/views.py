from django.contrib.auth.decorators import login_required
from django.shortcuts               import render

@login_required
def event_list(request):
    return render(request, 'events/list.html', { })
