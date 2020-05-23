from django.urls import path, include
from django.conf.urls import url
import users.views
from django.contrib import admin
from mainsys.views import homeView
from myadmin.views import shopView
import notifications.urls

urlpatterns = [
	path(r'admin/', admin.site.urls, name = "admin"),
    path(r'users/', users.views.index, name = 'users'),
    path(r'myadmin/', include('myadmin.urls')),
    path(r'lesson/', include('mainsys.urls')),
    path(r'forum/', include('Forum.urls')),
    path(r'', homeView.as_view(), name = 'home'),
    path(r'shop/', shopView.as_view(), name = 'shop'),
    path(r'notifications/', include(notifications.urls, namespace='notifications')),
    path(r'commends/', include('commends.urls')),
]