from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'Home/index.html')

@require_POST
@login_required
def mark_notifications_as_read(request):
    # Here you would implement the logic to mark notifications as read
    # For now, we'll just return a success response
    return JsonResponse({'status': 'success'})

@require_POST
@login_required
def clear_all_notifications(request):
    # Here you would implement the logic to clear all notifications
    # For now, we'll just return a success response
    return JsonResponse({'status': 'success'})