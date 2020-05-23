from django.shortcuts import render, redirect, reverse
from .ApaxChat import apax_chat
import json
from users.models import Parameter, UserProfile, boughtProduct
from django.views.generic.base import View 
from users.models import taskList, tradeRecord
from myadmin.models import product
from .alipay.alipay import get_payment
import time
import random
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import urllib
from django.db.models import Q
from notifications.models import *
# Create your views here.

class indexView(View):
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('myadmin_login')
		data = {}
		#图数据
		data['series'] = apax_chat()
		User = UserProfile.objects.get(username = request.user.get_username())
		Para = User.parameter_set.first()
		print(Para)
		#用户信息
		data['Para'] = Para
		return render(request, 'myadmin/index.html', data)
	
	def post(self, request):
		return redirect('myadmin_login')


def empty_page(request):
	return render(request, 'myadmin/empty_page.html')

def safe_account(request):
	if not request.user.is_authenticated or request.method == "POST":
		return redirect('myadmin_login')
	User = request.user
	exist_mobile = len(User.mobile) != 0
	exist_email = len(User.email) != 0
	return render(request, 'myadmin/SafeAccount.html', {'exist_mobile': exist_mobile, 'exist_email': exist_email})

def Shop_Cart(request):
	products = request.user.shoppingcart.product.all()
	total = 0
	for product in products:
		total += int(product.product_price)
	return render(request, 'myadmin/ShopCart.html', {"products": products, "total": total})

def Trasaction_Record(request):
	User = UserProfile.objects.get(username = request.user.get_username())
	Records = User.traderecord_set.all()[:50]
	for record in Records:
		record.Date = record.Date.strftime('%Y-%m-%d')
	return render(request, 'myadmin/TrasactionRecord.html', {"Records": Records})

class ChargeView(View):
	def get(self, request):
		return render(request, 'myadmin/charge.html')

	def post(self, request):
		# alipay = get_payment()
		if request.POST.get('value', None) != None:
			alipay = get_payment()
			num = request.POST.get('value', None)
			s = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
			User = UserProfile.objects.get(username = request.user.get_username())
			Ram = random.Random()
			s += str(User.id) + str(round(Ram.random() * 1000))
			url = alipay.get('支付EDU币%s元' % num, s, num)
			record = tradeRecord()
			record.recordId = s
			record.desc = '支付EDU币%s元' % num
			record.Total = num
			record.user = User
			record.save()
			return redirect(url)
		return render(request, 'myadmin/charge.html')
		
def system_mes(request):
	return render(request, 'myadmin/system_mes.html')

def mail_mes(request):
	try:
		unread = request.user.notifications.unread()
		return render(request, 'myadmin/mail_mes.html', {"unread": unread})
	except Exception as e:
		print(e.args)

def score_log(request):
	if not request.user.is_authenticated:
		return redirect('myadmin_login')
	User = UserProfile.objects.get(username = request.user.get_username())
	tasklist = User.tasklist_set.all()
	return render(request, 'myadmin/score_log.html', {"tasklist": tasklist})

class orderView(View):
	def get(self, request):
		Products = request.user.shoppingcart.product.all()
		total = 0
		for product in Products:
			total += int(product.product_price)
		Date = time.strftime('%Y-%m-%d', time.localtime())
		return render(request, 'myadmin/order.html', {"products": Products, "total": total, "Date": Date})
	
	def post(self, request):
		return JsonResponse({'status': 'Fail'}) 

class shopView(View):
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('myadmin_login')
		con = Q()
		con.connector = "OR"
		boughts = request.user.boughtproduct_set.all()
		for bought in boughts:
			con.children.append(('id', bought.product.id))
		Products = product.objects.filter(product_type = "四级", product_style = "单词").exclude(con)
		return render(request, 'myadmin/shop.html', {"Products": Products})
	
	def post(self, request):
		tyle = request.POST.get('type')
		style = request.POST.get('style')
		con = Q()
		con.connector = "OR"
		boughts = request.user.boughtproduct_set.all()
		for bought in boughts:
			con.children.append(('id', bought.product.id))
		Products = product.objects.filter(product_type = tyle, product_style = style).exclude(con)
		return render(request, 'myadmin/shop.html', {"Products": Products})

class varifiedView(View):
	def get(self, request):
		data = dict(request.GET)
		if data.get('out_trade_no', None) == None:
			return redirect('myadmin_index')
		record = tradeRecord.objects.get(recordId=data['out_trade_no'][0])
		if record.status == "成功支付":
			return redirect('myadmin_index')
		record.status = "成功支付"
		record.save()
		if "EDU币" in record.desc:
			User = UserProfile.objects.get(username = request.user.get_username())
			para = User.parameter_set.first()
			para.coins = str(int(para.coins) + int(record.Total))
			para.save()
		return redirect('myadmin_index')

	@csrf_exempt
	def post(self, request):
		print('异步回调')
		data = request.body.decode().split('=')
		if 'id' not in data or  len(data) != 2:
			return JsonResponse({'status': 'fail'})
		else:
			try:
				record = tradeRecord.objects.get(recordId = data[1])
				alipay = get_payment()
				url = alipay.get(record.desc, record.recordId, record.Total)
				res = urllib.request.urlopen(url)
				if '欢迎使用支付宝付款' in res.read().decode('gbk'):
					return JsonResponse({'status': 'redirect', 'url': url})
				record.status = "成功支付"
				record.save()
				User = UserProfile.objects.get(username = request.user.get_username())
				para = User.parameter_set.first()
				para.coins = str(int(para.coins) + int(record.Total))
				para.save()
				return JsonResponse({'status': 'success', 'id': data[1]})
			except Exception as e:
				return HttpResponse(e.args)

class user_books_View(View):
	def get(self, request):
		boughts = request.user.boughtproduct_set.all()
		return render(request, 'myadmin/user_books.html', {"boughts": boughts})
	
	def post(self, request):
		return render(request, 'myadmin/user_books.html')

def add_to_cart(request):
	if request.method == "GET":
		return JsonResponse({'status': 'Fail'})
	else:
		try:
			id = request.POST.get('id')
			cart = request.user.shoppingcart
			Product = product.objects.get(id = id)
			if not cart.product.filter(id = Product.id).exists():
				cart.product.add(Product)
				return JsonResponse({'status': 'success'})
			else:
				return JsonResponse({'status': 'Fail'})
		except Exception as e:
			print(e.args)

def del_cart_product(request):
	if request.method == "GET":
		return JsonResponse({'status': 'Fail'})
	else:
		try:
			id = request.POST.get('id')
			cart = request.user.shoppingcart
			Product = product.objects.get(id = id)
			cart.product.remove(Product)
			return JsonResponse({'status': "success"})
		except Exception as e:
			print(e.args)

def payBycoins(request):
	if request.method == 'POST':
		return JsonResponse({'status': 'Fail'})
	else:
		try:
			para = request.user.parameter_set.first()
			products = request.user.shoppingcart.product.all()
			total = 0
			for product in products:
				total += int(product.product_price)
			if total > int(para.coins):
				return redirect('order')
			para.coins = str(int(para.coins) - total)
			para.save()
			record = tradeRecord()
			s = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
			Ram = random.Random()
			s += str(request.user.id) + str(round(Ram.random() * 1000))
			record.recordId = s
			record.user = request.user
			record.Total = total
			record.desc = "购买了" + str(len(products)) + '件商品'
			record.status = "成功支付"
			record.save()
			for product in products:
				bought = boughtProduct()
				bought.product = product
				bought.user = request.user
				bought.save()
				request.user.shoppingcart.product.remove(product)
			return redirect('myadmin_index')
		except Exception as e:
			print(e.args)

def get_unread(request):
	try:
		unread = request.user.notifications.unread()
		total = []
		if unread != None:
			for x in unread:
				total.append({
					'timestamp': x.timestamp.__str__(),
					'actor': x.actor.username,
					'description': x.description,
					'id': x.id,
				})
		return JsonResponse({'unread': json.dumps(total), 'status': 'success'})
	except Exception as e:
		return HttpResponse('404 error')

def get_readed(request):
	try:
		unread = request.user.notifications.readed()
		return render(request, 'myadmin/mail_mes.html', {"unread": unread})
	except Exception as e:
		print(e.args)

def get_trash(request):
	try:
		unread = request.user.notifications.unread()
		return render(request, 'myadmin/mail_mes.html', {"unread": unread})
	except Exception as e:
		print(e.args)	
