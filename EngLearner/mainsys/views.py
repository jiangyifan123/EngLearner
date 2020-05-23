from django.shortcuts import render, redirect
from django.views.generic.base import View
import os
from .loadwords import load_excel
from myadmin.models import product, Task
from django.http import JsonResponse
import json
from users.models import boughtProduct, word_forget, words_log, taskList
from .models import *
import time
from .readSpider import RSpider
from .listen_spider import LSpider

class homeView(View):
	def get(self, request):
		return render(request, "mainsys/index.html")
	
	def post(self, request):
		return render(request, "mainsys/index.html")

class lessonView(View):
	def get(self,request):
		return render(request, "mainsys/lesson.html")

	def post(self,request):
		return render(request, "mainsys/lesson.html")

class listenView(View):
	def get(self,request):
		try:
			Data = listen_data.objects.all()
			Len = len(Data)
			return render(request, "mainsys/listen_page.html", {"listens": Data, "len": Len})
		except Exception as e:
			return HttpResponse(e.args)

	def post(self,request):
		return render(request, "mainsys/listen_page.html")

class readView(View):
	def get(self,request):
		readbooks = read_data.objects.all()
		return render(request, "mainsys/read_page.html", {"readbooks": readbooks})

	def post(self,request):
		return render(request, "mainsys/read_page.html")

class wordsView(View):
	def get(self,request):
		return render(request, "mainsys/words_page.html")

	def post(self,request):
		try:
			text = request.POST.get('text')
			boughts = request.user.boughtproduct_set.all()
			ans = []
			for bought in boughts:
				if bought.product.product_type == text and bought.product.product_style == "单词":
					ans.append(bought.product.product_name)
			return JsonResponse({"status": "success", "data": ans})
		except Exception as e:
			print(e.args)

class writeView(View):
	def get(self,request):
		return render(request, "mainsys/write_page.html")
	
	def post(self,request):
		try:
			text = request.POST.get('text')
			ft = product.objects.filter(product_type = text, product_style = "写作")
			ans = []
			if ft.exists():
				ans = [Product.product_name for Product in ft]
			return JsonResponse({"status": "success", "data": ans})
		except Exception as e:
			print(e.args)




class words_View(View):
	def get(self, request):
		return render(request, "mainsys/set_words.html")

	def post(self, request):
		return render(request, "mainsys/set_words.html")

class set_words_View(View):
	def post(self, request):
		product_name = request.POST.get('product_name')
		Product = None
		product_set = product.objects.filter(product_name = product_name)
		if product_set.exists():
			Product = product_set.first()
		else:
			Product = product()
			Type = request.POST.get('type')
			product_price = request.POST.get('product_price')
			product_description = request.POST.get('product_description')
			Product.product_name = product_name
			Product.product_type = Type
			Product.product_price = product_price
			Product.product_description = product_description
			Product.save()
		file = request.FILES.get('excel')
		if file == None or file.size > 2 * 1024 * 1024 or not file.name.endswith('xlsx'):
			return render(request, "mainsys/set_words.html")
		BaseDir = os.path.abspath(os.path.dirname(__file__))
		filedir = os.path.join(BaseDir, r'static\words\%s' % file.name)
		with open(filedir, 'wb') as f:
			for chunks in file.chunks():
				f.write(chunks)
		excel = load_excel(filedir)
		excel.get_content(Product)
		bought = boughtProduct()
		bought.product = Product
		bought = request.user
		bought.save()
		return render(request, "mainsys/set_words.html")
	
	def get(self, request):
		return render(request, "mainsys/set_words.html")

class word_indexView(View):
	def get(self, request):
		try:
			pos = request.GET.get('pos')
			book_name = request.session['word_book']
			Product = product.objects.get(product_name = book_name)
			if request.session.get('book_len') == None:
				len = request.session['book_len'] = Product.words_set.count()
			else:
				len = request.session['book_len']
			if pos == None:
				pos = 0
			else:
				pos = int(pos)
			if pos < 0 or pos > len:
				return JsonResponse({'error': "pos error"})
			Words = Product.words_set.all()[pos: pos + 20]
			return render(request, 'mainsys/word.html', {"words": Words, "pos": pos, "pos2": pos + 20})
		except Exception as e:
			return JsonResponse({'error': e.args})

	def post(self, request):
		try:
			book_name = request.POST.get('txt')
			request.session['word_book'] = book_name
			return redirect('word_index')
		except Exception as e:
			return JsonResponse({"error": e.args})

class test_View(View):
	def get(self, request):
		try:
			pos = request.GET.get('pos')
			book_name = request.session['word_book']
			Product = product.objects.get(product_name = book_name)
			if request.session.get('book_len') == None:
				len = request.session['book_len'] = Product.words_set.count()
			else:
				len = request.session['book_len']
			if pos == None:
				pos = 0
			else:
				pos = int(pos)
			if pos < 0 or pos > len:
				return JsonResponse({'error': "pos error"})
			Words = Product.words_set.all()[pos: pos + 20]
			return render(request, 'mainsys/test_page.html', {"words": Words, "pos": pos, "pos2": pos + 20})
		except Exception as e:
			return JsonResponse({'error': e.args})
	
	def post(self, request):
		try:
			word_name = request.POST.get('text')
			Word = words.objects.get(word = word_name)
			ft = word_forget.objects.filter(word = Word)
			if not ft.exists():
				wrong = word_forget()
				wrong.user = request.user
				wrong.word = Word
				wrong.save()
			else:
				wrong = ft.first()
				wrong.count += 1
				wrong.save()
			return JsonResponse({"status": "success"})
		except Exception as e:
			return JsonResponse({"status": e.args})

def upload_pos(request):
	if request.method == "GET":
		return JsonResponse({"status": "upload wrong"})
	else:
		try:
			book_name = request.session['word_book']
			if book_name == None:
				return JsonResponse({"status": e.args})
			pos = request.POST.get('pos')
			Product = product.objects.get(product_name = book_name)
			ft = request.user.words_log_set.filter(product_id = Product.id)
			if not ft.exists():
				log = words_log()
				log.user = request.user
				log.pos = pos
				log.product = Product
				log.save()
			else:
				log = ft.first()
				log.pos = pos
				log.save()
			task = Task.objects.get(taskname = "单词")
			Date = time.localtime()
			ft = request.user.tasklist_set.filter(taskDate__year = Date.tm_year, taskDate__month = Date.tm_mon, taskDate__day = Date.tm_mday, task_id = task.id)
			if not ft.exists():
				tasklist = taskList()
				tasklist.task = task
				tasklist.user = request.user
				tasklist.save()
			return JsonResponse({"status": "success"})
		except Exception as e:
			print(e.args)
			return JsonResponse({"status": e.args})

class write_detailView(View):
	def get(self, request):
		return render(request, 'mainsys/write_detail.html')

	def post(self, request):
		try:
			name = request.POST.get('txt')
			Product = product.objects.get(product_name = name)
			Write = Product.writes_set.first()
			return render(request, 'mainsys/write_detail.html', {"Write": Write})
		except Exception as e:
			print(e.args)

class write_addView(View):
	def get(self, request):
		return render(request, 'mainsys/write_add.html')

	def post(self, request):
		try:
			time = request.POST.get('time')
			title = request.POST.get('title')
			top = request.POST.get('top')
			problem = request.POST.get('problem')
			Type = request.POST.get('type')
			print(time, title, top, problem, Type)
			ft = product.objects.filter(product_name = title, product_style = "写作")
			if ft.exists():
				return render(request, 'mainsys/write_add.html', {"error": "标题重复"})
			else:
				Product = product()
				Product.product_name = title
				Product.product_price = 0
				Product.product_style = "写作"
				Product.description = "写作"
				Product.product_type = Type
				Product.save()
				Write_model = writes()
				Write_model.title = title
				Write_model.top = top
				Write_model.time = time
				Write_model.product = Product
				Write_model.problem = problem
				Write_model.save()
				return render(request, 'mainsys/write_add.html', {"error": "success"})
		except Exception as e:
			print(e.args)

def save_write(request):
	if request.method == "GET":
		return JsonResponse({'status': 'cannot use get method'})
	else:
		try:
			content = request.POST.get('content')
			id = request.POST.get('id')
			Write = writes.objects.get(id = id)
			ft = write_saving.objects.filter(user = request.user, writes = Write)
			if not ft.exists():
				saving = write_saving()
				saving.content = content
				saving.user = request.user
				saving.writes = Write
				saving.save()
			else:
				saving = ft.first()
				saving.content = content
				saving.save()
			return redirect('lesson_index')
		except Exception as e:
			print(e.args)

def update_read_books(request):
	if request.method == 'GET':
		return JsonResponse({'status': 'Fail'})
	else:
		try:
			spider = RSpider()
			ans = spider.get_list_text(spider.url)
			for i in ans:
				title = i['title']
				url = i['url']
				ft = read_data.objects.filter(url = url)
				if ft.exists():
					continue
				text, mp3_url = spider.get_all(url)
				eng = text[0]
				chinese = text[1]
				readbook = read_data()
				readbook.mp3_url = mp3_url
				readbook.eng = eng
				readbook.chinese = chinese
				readbook.title = title
				readbook.url = url
				readbook.save()
			return JsonResponse({'status': 'success'}) 
		except Exception as e:
			print(e.args)
			return JsonResponse({'status': 'Fail'})

class read_detailView(View):
	def get(self, request):
		try:
			id = request.GET.get('id')
			if id == None:
				return redirect('lesson_index')
			else:
				data = read_data.objects.get(id = id)
				combine = data.chinese + '\n' + data.eng
				return render(request, 'mainsys/read_detail.html', {"data": data, "combine": combine})
		except Exception as e:
			print(e.args)
			return redirect('lesson_index')
	
	def post(self, request):
		return render(request, 'mainsys/read_detail.html')

def listen_detail(request):
	if request.method == "POST":
		return JsonResponse({"status": "Fail"})
	else:
		try:
			id = request.GET.get('id')
			if id == None:
				return redirect('lesson_index')
			else:
				data = listen_data.objects.get(id = id)
				eng = data.eng.split(';')
				chinese = data.chinese.split(';')
				times = data.data_time.split(';')
				title = data.title
				mp3_url = data.mp3_url
				datas = []
				for pos in range(len(eng)):
					data = {}
					data['eng'] = eng[pos]
					data['chinese'] = chinese[pos]
					data['time'] = times[pos]
					datas.append(data)
				Len = len(datas)
				return render(request, 'mainsys/listen.html', {'title': title, 'datas': datas, "Len": Len, "mp3_url": mp3_url})
		except Exception as e:
			print(e.args)
			return JsonResponse({'status': 'Fail'})

def get_listen_data(request):
	try:
		spider = LSpider()
		menu = spider.get_url()
		for menu_url in menu:
			urls = spider.get_listen_url(menu_url)
			for url in urls:
				title = url[0]
				ft = listen_data.objects.filter(title = title)
				if ft.exists():
					continue
				url = url[1]
				all_eng, all_chinese, all_time = spider.get_all(url)
				all_time = ';'.join(all_time)
				all_eng = ';'.join(all_eng)
				all_chinese = ';'.join(all_chinese)
				data = listen_data()
				data.title = title
				data.url = url
				data.eng = all_eng
				data.chinese = all_chinese
				data.data_time = all_time
				print(len(all_eng), len(all_chinese))
				data.save()
		return JsonResponse({'status': 'success'})
	except Exception as e:
		return JsonResponse({'status': 'Fail'})
