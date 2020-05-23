from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.base import View
from .forms import RegisterForm, LoginForm
from .models import *
from myadmin.models import *
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.backends import ModelBackend
from django.urls import reverse
import json
import re

def index(request):
    return render(request, 'users/index.html')

class RegisterView(View):
	def get(self, request):
		error = ""
		return render(request, "myadmin/register.html", {"error": error})

	def post(self,request):
		register_form = RegisterForm(request.POST)
		if register_form.is_valid():
			username = request.POST.get("email", "")
			password = request.POST.get("password", "")
			try:
				if len(UserProfile.objects.filter(username = username)) != 0:
					return render(request, "myadmin/register.html", {"error": '已存在该用户名或邮箱'})
				user = UserProfile()
				user.username = username
				user.email = username
				user.password = make_password(password)
				user.save()
				task = Task.objects.get(taskname = "注册")
				TaskList = taskList(task = task, user = user)
				TaskList.save()
				para = Parameter(user = user)
				para.save()
				cart = shoppingCart()
				cart.user = user
				cart.save()
				print('注册成功')
			except Exception as e:
				print("注册失败")
				if e.args[1].startswith("Duplicate entry"):
					e.args = (e.args[0], "用户名重复")
				return render(request, "myadmin/register.html", {"error": e.args[1]})
			return redirect(reverse('myadmin_login'))
		else:
			for key, errors in register_form.errors.items():
				error = errors[0]
			return render(request, "myadmin/register.html", {"error": error})

class LoginView(View):
	def get(self, request):
		error = ""
		return render(request, "myadmin/login.html", {"error": error})

	def post(self, request):
		login_form = LoginForm(request.POST)
		if login_form.is_valid():
			username = request.POST.get('email', '')
			password = request.POST.get('password', '')
			try:
				user = UserProfile.objects.get(username = username)
			except Exception as e:
				user = None
			if user is not None and check_password(password, user.password):
				login(request, user)
				print('登陆成功: ', request.user.get_username())
				return redirect(reverse("myadmin_index"))
			else:
				error = ""
				if user == None:
					error += "用户名不存在"
				elif check_password(password, user.password):
					error += "密码不正确" 
				print(error)
				return render(request, 'myadmin/login.html', {"error": error})
		else:
			for key, errors in login_form.errors.items():
				error = errors[0]
			return render(request, "myadmin/login.html", {"error": error})

class LogoutBackend(View):
	def get(self, request):
		logout(request)
		return redirect('myadmin_login')

class forgotView(View):
	def get(self, request):
		return render(request, "myadmin/forgot.html")

