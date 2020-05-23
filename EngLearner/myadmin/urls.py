from django.urls import path
from . import views
from users.views import RegisterView, LoginView, LogoutBackend, forgotView
from .views import *


urlpatterns = [
	path('', indexView.as_view(), name = 'myadmin_index'),
	path('login/', LoginView.as_view(), name = 'myadmin_login'),
	path('register/', RegisterView.as_view(), name = 'myadmin_register'),
	path('empty_page/', views.empty_page, name = 'empty_page'),
	path('safe_account/', views.safe_account, name = "safe"),
	path('shop_cart/', views.Shop_Cart, name = "shop_cart"),
	path('trasaction_record/', views.Trasaction_Record, name = "trasaction_record"),
	path('charge/', ChargeView.as_view(), name = "charge"),
	path('system_mes/', views.system_mes, name = "system_mes"),
	path('mail_mes/', views.mail_mes, name = "mail_mes"),
	path('score_log/', views.score_log, name = "score_log"),
	path('order/', orderView.as_view(), name = "order"),
	path('logout/', LogoutBackend.as_view(), name = "logout"),
	path('forgot/', forgotView.as_view(), name = "forgot"),
	path('varified/', varifiedView.as_view(), name = "varified"),
	path('books/', user_books_View.as_view(), name = "user_books"),
	path('add_cart/', add_to_cart, name = "add_cart"),
	path('del_cart/', del_cart_product, name = "del_cart"),
	path('payBycoins/', payBycoins, name = "payBycoins"),
	path(r'get_unread', get_unread, name = 'get_unread'),
	path(r'get_readed', get_readed, name = 'get_readed'),
	path(r'get_trash', get_trash, name = 'get_trash'),
]