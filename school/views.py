from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Notification

# Create your views here.

def index(request):
    return render(request, "authentication/login.html")

@login_required
def dashboard(request):
    try:
        unread_notification = Notification.objects.filter(user=request.user, is_read=False)
        unread_notification_count = unread_notification.count()
    except:
        unread_notification = []
        unread_notification_count = 0
    return render(request, "Home/index.html", {
        'unread_notification': unread_notification,
        'unread_notification_count': unread_notification_count
    })

@login_required
def admin_dashboard(request):
    try:
        unread_notification = Notification.objects.filter(user=request.user, is_read=False)
        unread_notification_count = unread_notification.count()
    except:
        unread_notification = []
        unread_notification_count = 0
    return render(request, "Home/index.html", {
        'unread_notification': unread_notification,
        'unread_notification_count': unread_notification_count
    })

@login_required
def teacher_dashboard(request):
    try:
        unread_notification = Notification.objects.filter(user=request.user, is_read=False)
        unread_notification_count = unread_notification.count()
    except:
        unread_notification = []
        unread_notification_count = 0
    return render(request, "Home/index.html", {
        'unread_notification': unread_notification,
        'unread_notification_count': unread_notification_count
    })

@login_required
def student_dashboard(request):
    try:
        unread_notification = Notification.objects.filter(user=request.user, is_read=False)
        unread_notification_count = unread_notification.count()
    except:
        unread_notification = []
        unread_notification_count = 0
    return render(request, "Home/index.html", {
        'unread_notification': unread_notification,
        'unread_notification_count': unread_notification_count
    })

def mark_notification_as_read(request):
    if request.method == 'POST':
        try:
            notification = Notification.objects.filter(user=request.user, is_read=False)
            notification.update(is_read=True)
            return JsonResponse({'status': 'success'})
        except:
            return JsonResponse({'status': 'error', 'message': 'No notifications found'})
    return HttpResponseForbidden()

def clear_all_notification(request):
    if request.method == "POST":
        try:
            notification = Notification.objects.filter(user=request.user)
            notification.delete()
            return JsonResponse({'status': 'success'})
        except:
            return JsonResponse({'status': 'error', 'message': 'No notifications found'})
    return HttpResponseForbidden()

def clear_all_notifications(request):
    return HttpResponse('All notifications cleared (placeholder).')