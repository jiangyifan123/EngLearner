from django.shortcuts import render, redirect
from django.http import HttpResponse
from notifications.signals import notify
from django.contrib.auth.models import User

def send_msg(request):
    if not request.user.is_authenticated:
        return redirect('myadmin_login')
    notify.send(
        request.user,
        recipient = request.user,
        verb = "回复了你",
    )
    return HttpResponse('200 OK')