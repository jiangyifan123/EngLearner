from django.urls import include, path
from .views import *

urlpatterns = [
    path(r'', send_msg, name = "send_msg"),
]
